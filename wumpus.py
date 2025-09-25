
print("WUMPUS WORLD")

grid = [
    [[],     ['A'],        ['B'],     ['P'],       ['S']],
    [[],      ['B'],        [],      ['S', 'B'],   ['W']],
    [['B'],  ['P'],        ['B'],     [],          ['S']],
    [['P'],  ['G', 'B'],    ['P'],    ['B'],       ['B']],
    [['B'],  [''],          ['B'],   ['B'],        ['P']]
]


agent_position = [0,1];
while True:

  direction = input("Enter move (up/down/left/right): ");


  row, col = agent_position



  if direction == "up" and row > 0:
   agent_position[0] -= 1
  elif direction == "down" and row < 4:
    agent_position[0] += 1
  elif direction == "left" and col > 0:
    agent_position[1] -= 1
  elif direction == "right" and col < 4:
    agent_position[1] += 1
  else:
        print("❌ Invalid move! Try again.")
        continue
    
  new_row, new_col = agent_position
  cell_contents = grid[new_row][new_col]
  print("you Entered cell", cell_contents)

  if 'G' in cell_contents:
    print("🎉 You found the gold! You won!")
    break
  elif 'P' in cell_contents or 'W' in cell_contents:
    print("💀 You died!")
    break
  else:
    if 'B' in cell_contents:
        print("💨 You feel a Breeze! (Pit is nearby)")
    if 'S' in cell_contents:
        print("😷 You smell a Stench! (Wumpus is nearby)")
    if cell_contents == []:
        print("🟩 Nothing here. It's safe .")
print("🏁 Game over. Thanks for playing!")