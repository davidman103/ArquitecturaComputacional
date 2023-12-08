#include <iostream>
#include <utility>
#include <cmath>
#include <omp.h>
#include <iomanip>

using namespace std;

int main()
{

    // variables

    const int pasost = 200000, pasosx = 100;
    double tmax = 180, largo = 5;
    int T_i = 1000, t=1, h = 8,i;

    // deltas

    double dt = tmax / pasost;
    double dx = largo / pasosx;

    // difusividad termica (aluminio)
    float alfa = 0.0000988;

    cout << "Inicio de la simulacion :: datos de simulacion" << endl;
    cout << "largo = " << largo << " metros" << endl;
    cout << "Tiempo maximo de simulacion = " << tmax << " segundos" << endl;
    cout << "dx = " << dx << endl;
    cout << "dt = " << dt << endl;

    if (dt <= ((dx * dx) / 2))
    {
        double start = omp_get_wtime();
        omp_set_num_threads(h);
        static double T[pasost][pasosx];
        cout << "malla de simulacion de (" << pasost << "," << pasosx << ")" << endl;

        // condición inicial de la barra
    
        // condiciones de frontera y pasar todo a kelvin

        for (int i = 0; i < pasosx; i++)
        {
            T[0][i] = 273;

            for (int j = 0; j < pasost; j++)
            {   
                T[j][0] = T_i;
                T[j][pasosx - 1] = T_i;
            }
        }
        
        // Calculo de calor con diferencias finitas)

        while (t < pasost)     
        {
            #pragma omp parallel for
            for (i = 1; i < pasosx - 1; i++)
            {
                T[t][i] = T[t-1][i] + alfa * (dt / pow(dx, 2)) * (T[t-1][i+1] - 2 * T[t-1][i] + T[t-1][i-1]);
            }

            t++;
        }
        double end = omp_get_wtime();
        cout << endl;

        // muestra la malla inicial

        for (int j = 0; j < pasosx; j++)
        {
            cout << T[0][j] << " ";
        }

        cout << endl;

        // muestra la malla final

        for (int j = 0; j < pasosx; j++)
        {
            cout << T[pasost - 1][j] << " ";
        }

        
        cout << "Tiempo de ejecucion " << end - start << endl;
        return 0;
    }
    else
    {
        printf("Los parametros de dx y dt no permiten la convergencia.  Fin del programa");
        return 0;
    }
}