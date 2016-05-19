scale_length = input("what is the scale length in inches? ")
const = 17.817
number_of_frets = input("how many frets are there?")
fret_lengths = [];
x = 0
while x < number_of_frets:
     if x ==0:
          fret_position = scale_length/const
          fret_lengths.append(fret_position)
     if x !=0:
          new_scale_length = scale_length- fret_lengths[x-1]
          fret_pos = (new_scale_length / const)+ fret_lengths[x-1]
          fret_lengths.append(fret_pos)
     x+=1
y = 1
for lengths in fret_lengths:
     numb = str(y)
     print "Fret " + numb + ":"
     length = str(lengths)
     print length + " inches"
     y+=1


     
     
