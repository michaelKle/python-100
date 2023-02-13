# ascii art: https://ascii.co.uk/art/island

print(r'''
                                                    ____
                                         v        _(    )
        _ ^ _                          v         (___(__)
       '_\V/ `
       ' oX`
          X                            v
          X             -HELP!
          X                                                 .
          X        \O/                                      |\
          X.a##a.   M                                       |_\
       .aa########a.>>                                    __|__
    .a################aa.                                 \\   /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You are at a cross road. Where do you want to go? Type \"left\" or \"right\"\n").lower()

if choice1 != "left":
   print("You fell in a hole - game over!")
   print(r'''
        _.---,._,'
       /' _.--.<
         /'     `'
       /' _.---._____
       \.'   ___, .-'`
           /'    \\             .
         /'       `-.          -|-
        |                       |
        |                   .-'~~~`-.
        |                 .'         `.
        |                 |  R  I  P  |
  jgs   |                 |           |
        |                 |           |
         \              \\|           |//
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
''')
   exit()

choice2 = input("You have come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat or \"swim\"\n").lower()
if choice2 != "wait":
   print("You were eaten by a huge fish - game over!")
   print(r'''
    _///_
   /o    \/
   > ))_./\
      <
''')
   exit()

choice3 = input("You see a palace with 3 inviting doors. Which door do you open - \"red\", \"blue\" or \"yellow\"?\n").lower()
if choice3 != "yellow":
   print("There is a giant that eats you - game over")
   print(r'''
                               __.------._              _.----.____
                             .' -|  -   . `.        .--'           `--.
                            / '.' `-. `     \     .'                   `.
                           /  /      `.  ` \ \   /                       \
                          |  /         `.  \  | |    Who  are  you        |
                          |  |           `.   | |                         |
                          |  |.---.   .---.\  | |    calling  "little     |
                          | ||>< @>) (< @><|` | |                         |
                          |  |     / \     || |  \         one" ?       .'
                          |  |    ((_))    |  |   `  .-.             .-'
                          | `|`  /     \  '|  |   /.'   `-._______.-'
                          |  |   _.---._   |  |_.-'
                          /  \    `---'    /  |
                         /    `.    "    .'   \            o__
                        / / | | `-.___.-' ||   \          __)
                       /     '|           |  \  \          /
                      /'  /   |           |\   ` \
                     /   __.--'           `--.__  \
                    / .-' F  J `.       .' F  J `-.\
                   /.'   J   F   `.   .'   J   F   `.
                  .'     F  J      `.'      F  J     `.
                .'      J   F      (_)      J   F      `.
              .'        F  J                 F  J        `.
            .'         J   \                /    F         `.
          .'           F    `--.________.--'     J           `.
         /            /                           \            \
       .'            J                             F            `.
      /            .'|                             |`.            \
    .'           .'  F                             J  `.           `.
   /           .'    |                             |    `.           \
  (          .'      J                             F_     `.          )
   \       .'         \         /       \         /._`-._   `.       /
    \      \           `       '         `       '-._`-._`-._/      /
''')

print("You found the treasure - you win")
print(r'''

                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
''')