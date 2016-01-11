import os
import sys
from db import r
sys.path.append('models')
from question import Question

r.flushall()

Question(category='arts',
         question='What nationality was Chopin?',
         option_a='Russian',
         option_b='Polish',
         option_c='Chilean',
         option_d='French',
         answer='b').save()

Question(category='arts',
         question='Who lived at 221B, Baker Street, London?',
         option_a='Sir Arthur Conan Doyle',
         option_b='Nebil Kawas',
         option_c='Hercule Poirot',
         option_d='Sherlock Holmes',
         answer='d').save()

Question(category='arts',
         question='What Spanish artist said he would eat his wife when she died?',
         option_a='Patricio López',
         option_b='Salvador Dalí',
         option_c='Bernardo López Piquer',
         option_d='Esteban Vicente',
         answer='b').save()

Question(category='arts',
         question='Where did Salvador Dalí live?',
         option_a='Figueras',
         option_b='Santiago',
         option_c='London',
         option_d='Paris',
         answer='a').save()

Question(category='arts',
         question='Who wrote Julius Caesar, Macbeth and Hamlet?',
         option_a='Adrián Soto',
         option_b='Charlotte Brontë',
         option_c='Miguel de Cervantes',
         option_d='William Shakespeare',
         answer='d').save()

Question(category='arts',
         question='Who wrote Lazarillo de Tormes?',
         option_a='Gabriel García Márquez',
         option_b='Pablo Neruda',
         option_c='Anonymous',
         option_d='Jaime Castro',
         answer='c').save()

Question(category='arts',
         question='Who wrote the Ugly Duckling?',
         option_a='John Ugly',
         option_b='Fyodor Dostoyevsky',
         option_c='Hans Christian Andersen',
         option_d='Rudyard Kipling',
         answer='c').save()

Question(category='arts',
         question='Who wrote Dr. Jekyll and Mr. Hyde?',
         option_a='Ian Fleming',
         option_b='Robert Louis Stevenson',
         option_c='Sir Arthur Conan Doyle',
         option_d='George Orwell',
         answer='b').save()

Question(category='arts',
         question='Who wrote the James Bond books?',
         option_a='Ian Fleming',
         option_b='Sir Arthur Conan Doyle',
         option_c='Anonymous',
         option_d='George Orwell',
         answer='a').save()

Question(category='arts',
         question='What did the crocodile swallow in Peter Pan?',
         option_a='The Alarm Clock',
         option_b='Peter Pan',
         option_c='A Knife',
         option_d='A Cannonball',
         answer='a').save()

Question(category='arts',
         question='Where was Lope de Vega born?',
         option_a='Santiago',
         option_b='Barcelona',
         option_c='Madrid',
         option_d='Brasilia',
         answer='c').save()

Question(category='arts',
         question='What are the first three words of the bible?',
         option_a='Once upon a',
         option_b='In the beginning',
         option_c='Long time ago',
         option_d='In a galaxy',
         answer='b').save()

Question(category='arts',
         question="How many people went onto Noah's Ark?",
         option_a='3',
         option_b='5',
         option_c='8',
         option_d='9',
         answer='c').save()

Question(category='arts',
         question='Who painted the Mona Lisa?',
         option_a='Di Caprio',
         option_b='Da Vinci',
         option_c='Jan van Eyck',
         option_d='Donatello',
         answer='b').save()

Question(category='arts',
         question='Who painted the Sistine Chapel?',
         option_a='Descartes',
         option_b='Nakawas',
         option_c='Da Vinci',
         option_d='Michelangelo',
         answer='d').save()

Question(category='arts',
         question="What was the name of Don Quijote's horse?",
         option_a='Bucéfalo',
         option_b='Marengo',
         option_c='Rocinante',
         option_d='Comanche',
         answer='c').save()

Question(category='arts',
         question="Who was Robin Hood's girlfriend?",
         option_a='Maid Marian',
         option_b='Anne Boleyn',
         option_c='Eleanor of Aquitaine',
         option_d='Elizabeth of York',
         answer='a').save()

Question(category='arts',
         question='Who said, "I think, therefore I am"?',
         option_a='Napoleon',
         option_b='Descartes',
         option_c='Rousseau',
         option_d='Louis XIV',
         answer='b').save()

Question(category='arts',
         question='Where was El Greco born?',
         option_a='Greece',
         option_b='Florence',
         option_c='Milan',
         option_d='Rome',
         answer='a').save()

Question(category='arts',
         question='What was the first theatre play in Spain?',
         option_a='El Cantar de Roldán',
         option_b='Don Quijote de la Mancha',
         option_c='The Jungle Book',
         option_d='La Celestina',
         answer='d').save()

Question(category='entertainment',
         question="When was Elvis Presley's first ever concert?",
         option_a='1951',
         option_b='1952',
         option_c='1954',
         option_d='1955',
         answer='c').save()

Question(category='entertainment',
         question='What year did Elvis Presley die?',
         option_a='1974',
         option_b='1975',
         option_c='1976',
         option_d='1977',
         answer='d').save()

Question(category='entertainment',
         question='Who sang "My Way"?',
         option_a='Frank Sinatra',
         option_b='Elvis Presley',
         option_c='Michael Jackson',
         option_d='Nebil Kawas',
         answer='a').save()

Question(category='entertainment',
         question='How many oscars did Alfred Hitchcock win?',
         option_a='0',
         option_b='2',
         option_c='3',
         option_d='5',
         answer='a').save()

Question(category='entertainment',
         question='Who was the director of the film "Psycho"?',
         option_a='Michael Bay',
         option_b='Alfred Hitchcock',
         option_c='Steven Spielberg',
         option_d='Quentin Tarantino',
         answer='b').save()

Question(category='entertainment',
         question='In which city is Hollywood?',
         option_a='Hollywood',
         option_b='Washington, D.C.',
         option_c='New York',
         option_d='Los Angeles',
         answer='d').save()

Question(category='entertainment',
         question='Which of the following was NOT a member of the Beatles?',
         option_a='John Beatle',
         option_b='Ringo Starr',
         option_c='John Lennon',
         option_d='George Harrison',
         answer='a').save()

Question(category='geography',
         question='Which is the largest ocean?',
         option_a='Pacific',
         option_b='Atlantic',
         option_c='Indian',
         option_d='Arctic',
         answer='a').save()

Question(category='geography',
         question='Which is the smallest ocean?',
         option_a='Pacific',
         option_b='Atlantic',
         option_c='Indian',
         option_d='Arctic',
         answer='d').save()

Question(category='geography',
         question='What is the smallest country in the world?',
         option_a='Vatican City',
         option_b='Uruguay',
         option_c='Paraguay',
         option_d='Costa Rica',
         answer='a').save()

Question(category='geography',
         question='What is the capital of Honduras?',
         option_a='Caracas',
         option_b='Santo Domingo',
         option_c='Tegucigarpa',
         option_d='Addis Ababa',
         answer='c').save()

Question(category='geography',
         question='What is the capital of Ethiopia?',
         option_a='Caracas',
         option_b='Santo Domingo',
         option_c='Tegucigarpa',
         option_d='Addis Ababa',
         answer='d').save()

Question(category='geography',
         question='What is the capital of Australia?',
         option_a='Sidney',
         option_b='Canberra',
         option_c='Melbourne',
         option_d='Brisbane',
         answer='b').save()

Question(category='geography',
         question='What is the capital of Denmark?',
         option_a='Oslo',
         option_b='Aarhus',
         option_c='Rotterdam',
         option_d='Copenhagen',
         answer='d').save()

Question(category='geography',
         question='How many avenues radiate from the Arc de Triomphe in Paris?',
         option_a='8',
         option_b='10',
         option_c='12',
         option_d='14',
         answer='c').save()

Question(category='geography',
         question='Which river goes through London?',
         option_a='Thames',
         option_b='Po',
         option_c='Danube',
         option_d='Seine',
         answer='a').save()

Question(category='geography',
         question='Where are the Dolomites?',
         option_a='Argentina',
         option_b='France',
         option_c='Chile',
         option_d='Italy',
         answer='d').save()

Question(category='geography',
         question='What is the highest mountain in Africa?',
         option_a='Everest',
         option_b='Kilimanjaro',
         option_c='Pyrenees',
         option_d='Dolomites',
         answer='b').save()

Question(category='geography',
         question='What is the highest mountain in the world?',
         option_a='Everest',
         option_b='Kilimanjaro',
         option_c='Pyrenees',
         option_d='Dolomites',
         answer='a').save()

Question(category='geography',
         question='Which mountains are between Spain and France?',
         option_a='Everest',
         option_b='Kilimanjaro',
         option_c='Pyrenees',
         option_d='Dolomites',
         answer='c').save()

Question(category='geography',
         question='How many states are there in the United States of America?',
         option_a='50',
         option_b='51',
         option_c='52',
         option_d='53',
         answer='a').save()

Question(category='geography',
         question='Where are the Luxembourg Gardens?',
         option_a='Luxembourg',
         option_b='Berlin',
         option_c='Paris',
         option_d='London',
         answer='c').save()

Question(category='history',
         question='How many wives did Henry VIII have?',
         option_a='3',
         option_b='4',
         option_c='5',
         option_d='6',
         answer='d').save()

Question(category='history',
         question='When did the first man go into space?',
         option_a='1961',
         option_b='1965',
         option_c='1968',
         option_d='1969',
         answer='a').save()

Question(category='history',
         question='Who was the first man in space?',
         option_a='Yuri Gagarin',
         option_b='John Laika',
         option_c='Lance Armstrong',
         option_d='Neil Armstrong',
         answer='a').save()

Question(category='history',
         question='Who was the first man on the moon?',
         option_a='Yuri Gagarin',
         option_b='John Laika',
         option_c='Lance Armstrong',
         option_d='Neil Armstrong',
         answer='d').save()

Question(category='history',
         question='Where did the first atomic bomb explode for the first time in Japan?',
         option_a='Kyoto',
         option_b='Nagasaki',
         option_c='Tokyo',
         option_d='Hiroshima',
         answer='d').save()

Question(category='history',
         question='Who said, "Vini, vidi, vici"?',
         option_a='Napoleon',
         option_b='Caesar',
         option_c='Da Vinci',
         option_d='Shakespeare',
         answer='b').save()

Question(category='history',
         question='When did the American Civil War end?',
         option_a='1864',
         option_b='1865',
         option_c='1866',
         option_d='1867',
         answer='b').save()

Question(category='history',
         question='When did the Spanish Civil War end?',
         option_a='1917',
         option_b='1933',
         option_c='1939',
         option_d='1945',
         answer='c').save()

Question(category='history',
         question='When did the First World War start?',
         option_a='1914',
         option_b='1915',
         option_c='1917',
         option_d='1918',
         answer='a').save()

Question(category='history',
         question='When did the Second World War end?',
         option_a='1933',
         option_b='1937',
         option_c='1944',
         option_d='1945',
         answer='d').save()

Question(category='history',
         question='Who was the first president of USA?',
         option_a='Benjamin Franklin',
         option_b='Thomas Jefferson',
         option_c='John Adams',
         option_d='George Washington',
         answer='d').save()

Question(category='history',
         question="Who was Felipe el Hermoso's wife?",
         option_a='Mary I',
         option_b='Elizabeth I',
         option_c='Juana la Loca',
         option_d='Josephine',
         answer='c').save()

Question(category='history',
         question='In what decade was the last execution at the Tower of London?',
         option_a="1780's",
         option_b="1820's",
         option_c="1940's",
         option_d="1970's",
         answer='c').save()

Question(category='history',
         question="Where was Marco Polo's home town?",
         option_a='Genoa',
         option_b='Spain',
         option_c='Venice',
         option_d='Milan',
         answer='c').save()

Question(category='history',
         question='Where was Christopher Columbus born?',
         option_a='Genoa',
         option_b='Spain',
         option_c='Venice',
         option_d='Milan',
         answer='a').save()

Question(category='history',
         question='What year did Christopher Columbus go to America?',
         option_a='1453',
         option_b='1492',
         option_c='1504',
         option_d='1588',
         answer='b').save()

Question(category='history',
         question="What's the name of the famous big clock in London?",
         option_a='Big Bang',
         option_b='Big Ben',
         option_c='Eiffel',
         option_d='Entel',
         answer='b').save()

Question(category='history',
         question='What does the roman numeral C represent?',
         option_a='10',
         option_b='50',
         option_c='100',
         option_d='1000',
         answer='c').save()

Question(category='history',
         question='What did the Montgolfier brothers invent?',
         option_a='The Telephone',
         option_b='The Car',
         option_c='The Balloon',
         option_d='The Airplane',
         answer='c').save()

Question(category='other',
         question='What do the opposite sides of a 6-sided dice add up to?',
         option_a='7',
         option_b='8',
         option_c='9',
         option_d='10',
         answer='a').save()

Question(category='other',
         question='How many dots are there on two 6-sided dice?',
         option_a='20',
         option_b='21',
         option_c='40',
         option_d='42',
         answer='d').save()

Question(category='other',
         question='How many squares are there on a chess board?',
         option_a='32',
         option_b='64',
         option_c='128',
         option_d='256',
         answer='b').save()

Question(category='animals',
         question='How many legs has a spider got?',
         option_a='4',
         option_b='6',
         option_c='8',
         option_d='10',
         answer='c').save()

Question(category='science',
         question='What temperature does water boil at?',
         option_a='90ºC',
         option_b='100ºC',
         option_c='110ºC',
         option_d='120ºC',
         answer='b').save()

Question(category='science',
         question='What is the mass of a litre of water?',
         option_a='100g',
         option_b='1000g',
         option_c='10000g',
         option_d='100000g',
         answer='b').save()
