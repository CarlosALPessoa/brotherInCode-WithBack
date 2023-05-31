Instruções acerca do ambiente virtual. Obs: executar no terminal da pasta principal onde se encontra o manage.py <br>
 <br>
1º: <br>
python3 -m venv nome_do_ambiente_virtual <br>

2º: <br>
No windowns <br>
  .\nome_do_ambiente_virtual\Scripts\activate.ps1 <br>
No Linux: <br>
  source nome_do_ambiente_virtual/bin/activate <br>
  
3º: <br>
pip install -r requements.txt <br>

4º: <br>
py manage.py migrate <br>
py manage.py runserver
