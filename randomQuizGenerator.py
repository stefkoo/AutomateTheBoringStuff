#! python3
# randomQuizGenerator.py - Erstellt Testfragebogen mit Fragen und Antworten
# in zufälliger Reihenfolge sowie die zugehörigen Lösungsbogen

import random

# Die abzufragenden Dateien. Die Schlüssel sind die Bundesstaaten, die Werte
# deren Hauptstädte

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
   'NewMexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus',
   'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
   'WestVirginia': 'Charleston','Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# erstellt 35 Fragebögen
for quizNum in range(2):
   # Dateien für Frage und Lösungen erstellen
   quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
   answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

   #Kopf für den Test schreiben
   quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
   quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum +1))
   quizFile.write('\n\n')


   #Reihenfolge der Bundesstaaten durcheinanderwürfeln
   states = list(capitals.keys())
   random.shuffle(states)


   #Alle 50 Staaten durchlaufen und für jeden eine Frage stellen
   for questionNum in range(50):
      #ruft die richtigen und falschen Antworten ab
      correctAnswer = capitals[states[questionNum]]
      wrongAnswer = list(capitals.values())
      del wrongAnswer[wrongAnswer.index(correctAnswer)]
      wrongAnswer = random.sample(wrongAnswer, 3)
      answerOptions = wrongAnswer + [correctAnswer]
      random.shuffle(answerOptions)

      #Fragen und mögliche Antworten in die Textdatei schreiben
      quizFile.write('%s. What is the capital of %s?\n' % (questionNum +1, states[questionNum]))
      for i in range(4):
         quizFile.write('     %s. %s\n' % ('ABCD'[i], answerOptions[i]))
      quizFile.write('\n')



      #Lösungsschlüssel in die Datei schreiben
      answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
   quizFile.close()
   answerKeyFile.close()

