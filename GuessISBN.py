import sqlite3

import nltk

nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import numpy as np

connection = sqlite3.connect(r"C:\Users\Josh\COUNTER-5-Report-Tool\all_data\search\search.db")
cursor = connection.cursor()

cursor.execute("SELECT title FROM TR")
stop_words = set(stopwords.words('english'))
keywords = {
    'Accounting': ['accounting', 'financial statements', 'taxes', 'auditing', 'bookkeeping', 'finance',
                   'financial analysis', 'budgeting', 'cost management', 'business law', 'forensic accounting',
                   'managerial accounting', 'financial reporting', 'internal controls', 'payroll'],
    'Criminal Justice': ['criminal justice', 'law enforcement', 'crime prevention', 'corrections', 'criminal law',
                         'criminal investigation', 'criminology', 'forensic science', 'juvenile justice',
                         'criminal procedure', 'homeland security', 'policing', 'victimology', 'criminal behavior',
                         'crime analysis'],
    'Business Management': ['business management', 'leadership', 'strategic planning', 'organizational behavior',
                            'business strategy', 'project management', 'entrepreneurship', 'business ethics',
                            'change management', 'human resource management', 'operations management',
                            'supply chain management', 'business communication', 'decision-making',
                            'business analysis'],
    'Digital Content Creation': ['digital content creation', 'content marketing', 'social media marketing',
                                 'copywriting', 'content strategy', 'video production', 'graphic design',
                                 'branding', 'web design', 'search engine optimization', 'digital storytelling',
                                 'creative writing', 'content creation tools', 'visual communication',
                                 'user experience'],
    'Psychology': ['psychology', 'mental health', 'counseling', 'behavioral psychology', 'cognitive psychology',
                   'social psychology', 'developmental psychology', 'abnormal psychology', 'personality',
                   'psychotherapy', 'research methods', 'psychological assessment', 'neuropsychology',
                   'forensic psychology', 'positive psychology'],
    'Critical Race and Ethnic Studies': ['critical race and ethnic studies', 'race', 'ethnicity', 'racism',
                                         'racial inequality', 'social justice', 'intersectionality',
                                         'critical theory', 'colonialism', 'white supremacy', 'identity politics',
                                         'decolonization', 'postcolonialism', 'racialized experiences',
                                         'racial identity'],
    'Social Change': ['social change', 'community development', 'social activism', 'advocacy', 'policy',
                      'social movements', 'inequality', 'justice', 'sustainability', 'human rights', 'empowerment',
                      'collective action', 'grassroots organizing', 'community engagement', 'social innovation'],
    'Data Science': ['data science', 'data analysis', 'machine learning', 'data visualization', 'statistics',
                     'predictive modeling', 'big data', 'data mining', 'programming', 'database management',
                     'data-driven decision making', 'statistical modeling', 'data manipulation',
                     'data interpretation', 'data storytelling'],
    'Art: Studio': ['art', 'studio art', 'painting', 'drawing', 'sculpture', 'printmaking', 'ceramics',
                    'photography', 'mixed media', 'installation art', 'conceptual art', 'artistic techniques',
                    'art history', 'creative process', 'art criticism'],
    'Marketing': ['marketing', 'advertising', 'branding', 'market research', 'digital marketing', 'consumer behavior',
                  'marketing strategy', 'social media marketing', 'public relations', 'marketing analytics',
                  'marketing communications', 'product management', 'marketing campaigns', 'content marketing',
                  'brand management'],
    'Secondary Education Program': ['secondary education', 'teaching', 'curriculum development', 'classroom management',
                                    'lesson planning', 'educational psychology', 'adolescent development',
                                    'teaching strategies', 'assessment and evaluation', 'inclusive education',
                                    'educational technology', 'student engagement', 'differentiated instruction',
                                    'learning theories', 'teaching methodologies'],
    'Chemistry': ['chemistry', 'chemical reactions', 'organic chemistry', 'inorganic chemistry', 'physical chemistry',
                  'analytical chemistry', 'biochemistry', 'laboratory techniques', 'quantum mechanics', 'chemical bonding',
                  'chemical kinetics', 'spectroscopy', 'thermodynamics', 'stoichiometry', 'chemical equations'],
    'Computer Science & Information Technology': ['computer science', 'programming', 'algorithms', 'data structures',
                                                  'software development', 'web development', 'database systems',
                                                  'networking', 'artificial intelligence', 'machine learning',
                                                  'cybersecurity', 'computer architecture', 'operating systems',
                                                  'data science', 'computer graphics'],
    'Peace and Social Transformation': ['peace', 'conflict resolution', 'social transformation', 'peacebuilding',
                                        'nonviolence', 'reconciliation', 'peace education', 'human rights',
                                        'social justice', 'intercultural communication', 'community development',
                                        'restorative justice', 'gender and peacebuilding', 'peace advocacy',
                                        'conflict analysis'],
    'Physical Therapy': ['physical therapy', 'rehabilitation', 'musculoskeletal disorders', 'pain management',
                         'therapeutic exercises', 'neurological conditions', 'orthopedics', 'sports injuries',
                         'geriatric physical therapy', 'cardiopulmonary rehabilitation', 'pediatric physical therapy',
                         'physical therapy assessments', 'gait analysis', 'kinesiology', 'therapeutic modalities'],
    'Elementary Education (Independence)': ['elementary education', 'teaching', 'elementary curriculum',
                                            'classroom management', 'lesson planning', 'child development',
                                            'literacy instruction', 'mathematics instruction', 'science instruction',
                                            'social studies instruction', 'inclusive education', 'educational technology',
                                            'assessment and evaluation', 'differentiated instruction', 'student engagement'],
    'Data Science and Analytics': ['data science', 'data analytics', 'machine learning', 'data visualization',
                                   'statistical analysis', 'predictive modeling', 'data mining', 'programming',
                                   'database management', 'business intelligence', 'data-driven decision making',
                                   'data manipulation', 'data interpretation', 'data storytelling', 'data governance'],
    'Sustainability Studies': ['sustainability', 'environmental science', 'ecology', 'renewable energy',
                               'sustainable development', 'climate change', 'environmental policy',
                               'sustainable agriculture', 'conservation biology', 'environmental justice',
                               'green technology', 'ecosystems', 'environmental ethics', 'social responsibility',
                               'sustainable urban planning'],
    'Women’s, Gender, and Sexuality Studies': ['women’s studies', 'gender studies', 'sexuality studies',
                                               'feminist theory', 'intersectionality', 'gender identity',
                                               'sexual orientation', 'reproductive rights', 'masculinity',
                                               'feminist activism', 'queer theory', 'gender inequality',
                                               'feminist literature', 'gender and politics', 'sexism'],
    'Agricultural Business': ['agricultural business', 'agribusiness', 'agricultural economics', 'food systems',
                              'farm management', 'agricultural marketing', 'rural development', 'sustainable agriculture',
                              'supply chain management', 'agricultural policy', 'international agriculture',
                              'commodity markets', 'agricultural finance', 'agricultural law'],
    'Sociology': ['sociology', 'social structure', 'social inequality', 'social change', 'sociological theory',
                  'social institutions', 'social movements', 'race and ethnicity', 'gender and sexuality',
                  'social research methods', 'sociological perspectives', 'socialization', 'family and marriage',
                  'deviance and crime', 'social stratification'],
    'Art: Graphic Design': ['art', 'graphic design', 'typography', 'branding', 'layout design', 'illustration',
                            'digital media', 'color theory', 'visual communication', 'user experience design',
                            'print design', 'web design', 'motion graphics', 'logo design', 'creative process'],
    'Nutrition and Human Performance': ['nutrition', 'exercise science', 'human performance', 'dietetics',
                                        'sports nutrition', 'nutritional biochemistry', 'public health nutrition',
                                        'weight management', 'nutrition education', 'nutritional assessment',
                                        'nutrigenomics', 'metabolism', 'vitamins and minerals', 'diet and disease',
                                        'nutrition counseling'],
    'Sport Management': ['sport management', 'sports marketing', 'event management', 'athletic administration',
                         'sports law', 'facility management', 'sports finance', 'sports sponsorship',
                         'sports analytics', 'sports governance', 'sports ethics', 'sport and society',
                         'intercollegiate athletics', 'revenue generation', 'sports media'],
    'Organizational Leadership': ['organizational leadership', 'leadership theory', 'change management',
                                  'strategic planning', 'organizational behavior', 'team dynamics', 'decision-making',
                                  'communication skills', 'conflict resolution', 'ethical leadership', 'emotional intelligence',
                                  'leadership styles', 'organizational culture', 'organizational development',
                                  'leadership ethics'],
    'Religion': ['religion', 'religious studies', 'theology', 'comparative religion', 'world religions',
                 'philosophy of religion', 'religious ethics', 'spirituality', 'religious traditions',
                 'religious texts', 'religious practices', 'religious identity', 'interfaith dialogue',
                 'religion and society', 'religious diversity'],
    'Interdisciplinary Studies': ['interdisciplinary studies', 'cross-disciplinary', 'multidisciplinary',
                                  'integrative learning', 'holistic approach', 'interdisciplinary research',
                                  'critical thinking', 'problem-solving', 'collaboration', 'systems thinking',
                                  'interdisciplinary perspectives', 'innovation', 'creative problem solving',
                                  'knowledge integration', 'interdisciplinary communication'],
    'Coaching': ['coaching', 'leadership coaching', 'executive coaching', 'performance coaching', 'life coaching',
                 'personal development', 'communication skills', 'goal setting', 'motivation', 'emotional intelligence',
                 'positive psychology', 'self-discovery', 'behavior change', 'career coaching', 'coaching techniques'],
    'Biology: General': ['biology', 'cell biology', 'genetics', 'evolution', 'ecology', 'physiology', 'molecular biology',
                         'biochemistry', 'microbiology', 'botany', 'zoology', 'anatomy', 'developmental biology',
                         'biotechnology', 'scientific research'],
    'Physical Education and Health': ['physical education', 'health education', 'human anatomy', 'exercise physiology',
                                      'movement education', 'fitness and wellness', 'motor development',
                                      'nutrition and health', 'sports and games', 'stress management',
                                      'injury prevention', 'personal fitness', 'health promotion',
                                      'health behavior', 'lifespan development'],
    'History': ['history', 'world history', 'European history', 'American history', 'ancient history',
                'medieval history', 'modern history', 'historical research', 'historiography',
                'historical analysis', 'historical interpretation', 'historical events',
                'historical figures', 'social history', 'cultural history'],
    'Transformational Leadership': ['transformational leadership', 'change management', 'leadership development',
                                    'visionary leadership', 'ethical leadership', 'emotional intelligence',
                                    'team building', 'leadership communication', 'organizational culture',
                                    'strategic planning', 'innovation and creativity', 'leadership theories',
                                    'leadership styles', 'leading change', 'leadership ethics']
}


batch_size = 999
column_check_query = "PRAGMA table_info(TR)"
cursor.execute(column_check_query)
columns = cursor.fetchall()
column_exists = any(column[1] == 'most_probable_major' for column in columns)

# If the column doesn't exist, add it to the table
if not column_exists:
    add_column_query = "ALTER TABLE TR ADD COLUMN most_probable_major VARCHAR(255)"
    cursor.execute(add_column_query)
    connection.commit()
    print("Column 'most_probable_major' added successfully.")
else:
    print("Column 'most_probable_major' already exists in the table.")


def UpdateRows(unused):

    count = 0
    # cursor.execute("Select Title from TR where most_probable_major = 'Unorganized'")
   #while  ((len(cursor.fetchall()))>1):
    while True:
        cursor.execute("Select Title from TR where most_probable_major = 'SortMe'")
        count+=1
        rows = cursor.fetchmany(batch_size)
        if not rows:
            break

        for row in rows:

            title = row[0]

            tokens = word_tokenize(title)
            filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
            matches = {}
            for major, major_keywords in keywords.items():
                match_count = np.sum([1 for token in filtered_tokens if token.lower() in major_keywords])
                matches[major] = match_count
            most_probable_major = max(matches, key=matches.get)

            if most_probable_major == 'SortMe':
                count += 1
                unused.append(filtered_tokens)

            update_query = r'UPDATE TR SET most_probable_major = "' + most_probable_major.replace('"', '""') + '" WHERE title = "' + title.replace('"', '""').replace("'", "''") + '"'

            cursor.execute(update_query)

        connection.commit()

        break
        #cursor.execute("Select Title from TR where most_probable_major = 'Unorganized'")
unused= []
UpdateRows(unused)
#print(cursor.fetchall())
cursor.execute("Select Title from TR where most_probable_major = 'Unorganized'")

print(len(cursor.fetchall()))

cursor.close()
connection.commit()
connection.close()
