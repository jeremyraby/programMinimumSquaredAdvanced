# import modules
from random import randint, choice
import datetime

# define functions
def swing():
  '''Determine which swing progression to do based on skill level'''
  if level == 'b':
    drill = randint(1,2)
    if drill == 1:
      return 'Deadlifts'
    elif drill == 2:
      return 'Dead-stop Swings'
  elif level == 'i':
    drill = randint(1, 4)
    if drill == 1:
      return 'Deadlifts'
    elif drill == 2:
      return 'Dead-stop Swings'
    elif drill == 3:
      return 'Two-hand Swings'
    elif drill == 4:
      return 'One-hand Swings'
  else:
    drill = randint(1,6)
    if drill == 1:
      return 'Deadlifts'
    elif drill == 2:
      return 'Dead-stop Swings'
    elif drill == 3:
      return 'Two-hand Swings'
    elif drill == 4:
      return 'One-hand Swings'
    elif drill == 5:
      return 'Hand-to-hand Swings'
    else:
      return 'Double Swings'

def getup():
  '''Determine which get-up progression to do based on skill level'''
  if level == 'b':
    drill = randint(1,2)
    if drill == 1:
      return 'Arm-bars'
    elif drill == 2:
      return 'Floor Presses'
  elif level == 'i':
    drill = randint(1, 4)
    if drill == 1:
      return 'Arm-bars'
    elif drill == 2:
      return 'Floor Presses'
    elif drill == 3:
      return 'Roll-to-elbow Get-ups'
    elif drill == 4:
      return 'Tall-sit Get-ups'
  else:
    drill = randint(1, 6)
    if drill == 1:
      return 'Arm-bars'
    elif drill == 2:
      return 'Floor Presses'
    elif drill == 3:
      return 'Roll-to-elbow Get-ups'
    elif drill == 4:
      return 'Tall-sit Get-ups'
    elif drill == 5:
      return 'Tactical Lunge Get-ups'
    else:
      return 'Full Get-ups'

def bent_press():
  '''Determine which bent press progression to do based on skill level'''
  if level == 'b':
    drill = randint(1, 2)
    if drill == 1:
      return 'Bent Arm-bars'
    elif drill == 2:
      return 'Half-kneeling Windmills'
  elif level == 'i':
    drill = randint(1, 4)
    if drill == 1:
      return 'Bent Arm-bars'
    elif drill == 2:
      return 'Half-kneeling Windmills'
    elif drill == 3:
      return 'Low Windmills'
    elif drill == 4:
      return 'High Windmills'
  else:
    drill = randint(1, 6)
    if drill == 1:
      return 'Bent Arm-bars'
    elif drill == 2:
      return 'Half-kneeling Windmills'
    elif drill == 3:
      return 'Low Windmills'
    elif drill == 4:
      return 'High Windmills'
    elif drill == 5:
      return 'Bent Presses'
    else:
      return 'Two Hands Anyhow'

def snatch():
  '''Determine which snatch progression to do based on skill level'''
  if level == 'b':
    drill = randint(1, 2)
    if drill == 1:
      return 'One-Hand Swings'
    elif drill == 2:
      return 'High Pulls'
  elif level == 'i':
    drill = randint(1, 4)
    if drill == 1:
      return 'One-Hand Swings'
    elif drill == 2:
      return 'High Pulls'
    elif drill == 3:
      return 'Dead-stop Snatches'
    elif drill == 4:
      return 'Tempo Snatches'
  else:
    drill = randint(1,6)
    if drill == 1:
      return 'One-Hand Swings'
    elif drill == 2:
      return 'High Pulls'
    elif drill == 3:
      return 'Dead-stop Snatches'
    elif drill == 4:
      return 'Tempo Snatches'
    elif drill == 5:
      return 'Heavy Snatches (2-3 reps with a 5 rm size bell)'
    else:
      return 'Double Snatches'

def volume():
  '''Determine how long the exercise sets will last'''
  dice = randint(1, 6) * 2
  return dice

def warmup():
  '''Determine how many warm-up sets to do based on skill level'''
  if level == 'b':
    return 1
  elif level == 'i':
    return 2
  else:
    return 3

def warm_up_reps():
  '''Determine how many reps to do in the warm-up based on skill level'''
  if level == 'b':
    return 5
  elif level == 'i':
    return 8
  else:
    return 10

def ball_reps():
  '''Determine how many reps of the ballistic movement to do per set based on skill level'''
  if level == 'b':
    return 5
  elif level == 'i':
    return 7
  else:
    return 10

def grind_reps():
  '''Determine how many reps of the grind movement to do per set based on skill level'''
  if level == 'b':
    return 3
  elif level == 'i':
    return 2
  else:
    return 1

def upper_mobility():
  upper_drills = ['arm bars', 'bent arm bars', 'Bretzel', 'kneeling lat stretch', 'cat/cow', 'cobra', 'scap pushups', 'tabletop', 'l-arm stretch', 'half-kneeling windmills','GMB wrist series']

  upper_drill = choice(upper_drills)
  return upper_drill

def lower_mobility():
  lower_drills = ['hamstring stretch n glide', '90/90', 'QL', 'KB good morning','tactical frog', 'RKC lunge', 'prying goblet squats', 'piriformis stretch', 'ankle circles']

  lower_drill = choice(lower_drills)
  return lower_drill

# main program
today = datetime.date.today()
today = today.isoweekday()

level = input('What level are you? (b/i/a) ')
level = level.lower()

print('_' * 32)

print(f'''\nWarm-up with {warmup()} sets of halos, \nsquats, and bridges for {warm_up_reps()} reps \neach.\n''')

if today == 1 or today == 4:
  print(f'Do {swing()} and {getup()} for {volume()} minutes.')
elif today == 2 or today == 5:
  print(f'Do {snatch()} and {bent_press()} for {volume()} minutes each.')
else:
  print(f'Do {upper_mobility()} & {lower_mobility()} for {volume()} minutes.')

print('_' * 32)

print(f'''\nBallistics = {ball_reps()} reps/set\nGrinds = {grind_reps()} reps/set\nArm-bars = 5 breaths/set''')