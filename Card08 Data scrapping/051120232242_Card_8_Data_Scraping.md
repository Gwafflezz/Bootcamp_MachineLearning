## Basic Data Scraping

#### 1 teste: métodos de leitura 


```python
from bs4 import BeautifulSoup

with open('home.html','r') as html_file:

    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')

    courses_html_tags = soup.find_all('h5')

    for course in courses_html_tags:

        print(course.text)
```

#### 2 teste: leitura de informações específicas 
```python
from bs4 import BeautifulSoup

  

with open('home.html','r') as html_file:

    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')

    course_cards = soup.find_all('div',class_ = 'card')

    for course in course_cards:

        course_name = course.h5.text

        course_price = course.a.text.split()[-1]

  

        print(f'{course_name} costs {course_price}')
```

#### 3) Aquisição de informações de vagas,TimesJobs

```python 

from bs4 import BeautifulSoup
import requestslazy riv
import time     

print('Put some skill you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():

    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li',class_ = 'clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find('span',class_ = 'sim-posted').span.text

        if 'few' in published_date:      
            company_name = job.find('h3',class_ = 'joblist-comp-name').text.replace(' ','')
            skills = job.find('span',class_ = 'srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']

            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                        
                    f.write(f"Company Name: {company_name.strip()}\n")
                    f.write(f"Required Skills: {skills.strip()}\n\")
                    f.write(f'More Info: {more_info}')
                print(f'File Saved:{index}')

                print('')
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'waiting {time_wait} minutes..')
        time.sleep(time_wait * 60)

```

##### Funcionamento:

1. Importação de bibliotecas:
    
    - O código começa importando as bibliotecas necessárias: `BeautifulSoup` para análise HTML e `requests` para fazer solicitações HTTP. Também importa a biblioteca `time` para controlar o intervalo entre as consultas.
2. Solicitação da entrada do usuário:
   
    - Solicita ao usuário que insira uma habilidade da qual ele não está familiarizado. Isso será usado para filtrar os empregos que não exigem essa habilidade.
3. Função `find_jobs`:
    
    - Define uma função chamada `find_jobs` que realiza a pesquisa de empregos e a filtragem.
    - Faz uma solicitação HTTP para a página de pesquisa de empregos do TimesJobs.
    - Analisa o conteúdo HTML da página usando BeautifulSoup.
    - Localiza todos os elementos de emprego no HTML.
4. Loop de empregos:
    
    - Itera sobre a lista de empregos encontrados.
    - Extrai a data de publicação, o nome da empresa, as habilidades necessárias e um link para obter mais informações sobre o emprego.
5. Filtragem de empregos:
    
    - Verifica se a palavra "few" está na data de publicação (indicando empregos recentes).
    - Se a habilidade não familiar do usuário não estiver nas habilidades necessárias para o emprego, o emprego é considerado relevante.
    - Os detalhes relevantes do emprego são escritos em um arquivo de texto no diretório 'posts'.
6. Loop infinito:
    
    - O código continua pesquisando empregos em um loop infinito.
    - Após cada consulta, ele aguarda por um período especificado (10 minutos) antes de fazer a próxima pesquisa.


 