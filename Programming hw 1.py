#Adolfo Martinez
#CS151-05 Prof. Mehri
#9/22/21
#Programming assignment: 1
#This program will tell total area of the walls and ceiling of a room and the necessary amount of paint and primer to cover the room
#Input: Room dimensions
#Output: Total area and Paint/Primer needed

wall_l = int(input("What is the length of you wall in feet?:"))
wall_w = int(input("And what is the width of your wall in feet?:"))
wall_h = int(input("Finally what is the height of your wall in feet?:"))

t_area = (((wall_l * wall_h)*4)+(wall_l**2))

primer_need = ((t_area//200)+1)
paint_need = ((t_area//350)+1)

print("The total area you're going to need to paint is", t_area, "sq.ft and you will need", primer_need, "gallons of primer and", paint_need, "gallons of paint.")