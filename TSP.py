import typer
from rich import print
import numpy as np
import pandas as pd
app = typer.Typer()


@app.command()
def create_random_data(num_points: int=10, PDF:str = 'normal'):
    if PDF=='normal':
        coordinates=np.random.normal(loc=0,scale=1,size=(num_points,2))
    if PDF=='random':
        coordinates=np.random.random(size=(num_points,2))
    else:
        print(f'[red]PDF {PDF} inválida [red\]')
        raise typer.Exit()
    data=np.zeros((num_points,num_points))
    for i in range(num_points):
        for j in range(num_points):
            data[i][j]=np.linalg.norm(coordinates[i]-coordinates[j])
    np.savetxt('banco_de_dados//matrizes//matriz_aleatoria.txt',data)
    df=pd.DataFrame(coordinates,columns=['x_value','y_value'])
    df.to_csv('banco_de_dados//coords//coord_aleatoria.csv')
    print('Dados aleatórios criados com sucesso!')

@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


if __name__ == "__main__":
    app()