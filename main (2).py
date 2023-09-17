''' Implement a class called player that represent a cricket player. The player should have a method called play() which prints "The player is playing cricket.Drive two classes,Batsman and Bowler, from the player class.override the play() method in each derived class to print "The batsman is batting " and "The bowler is bowling ", respectively.write a program to create objects of both the Batsman and Bowler classes and call the play() method for each object.'''


class Player:
  def play(self):
    print("The player is playing cricket.")

class Batsman(Player):
  def play(self):
    print("The batsman is bating.")

class Bowler(Player):
  def play(self):
    print("The bowler is bowling.")

# create object of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# call the play() mathod for each object
batsman.play()
bowler.play()