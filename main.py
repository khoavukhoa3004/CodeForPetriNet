from PetriClass import *
def SolvingPro_1():
   return True

def SolvingPro_2():
   return True



def SolvingPro_3():
   print("Nhap luong nguoi o")
   while True:
      try:
         wait = int(input("wait: "))
         if wait < 0:
            print("Gia tri am, vui long nhap lai!")
            continue
         free = int(input("free: "))
         if free < 0:
            print("Gia tri am, vui long nhap lai!")
            continue
         busy = int(input("busy: "))
         if busy < 0:
            print("Gia tri am, vui long nhap lai!")
            continue
         inside = int(input("inside: "))
         if inside < 0:
            print("Gia tri am, vui long nhap lai!")
            continue
         done = int(input("done: "))
         if done < 0:
            print("Gia tri am, vui long nhap lai!")
            continue
         document = int(input("document: "))
         if document < 0:
            print("Gia tri am, vui long nhap lai!")
            continue
         break
      except ValueError:
         print("Gia tri khong hop le! Vui long nhap lai...")

   # Tao tap chua cac place va token
   ps = [Place("wait",wait ), Place("free",free), Place("busy", busy), Place("inside",inside),
         Place("done",done)  , Place("document",document)]
   
   # Tao tap chua cac transition (co ca edge In va edge Out)
   ts =[Transition("start",[In(ps[0]), In(ps[1])],[Out(ps[2]), Out(ps[3])]),

        Transition("change",[In(ps[2]), In(ps[3])],[Out(ps[4]), Out(ps[5])]),

        Transition("end",[In(ps[5])], [Out(ps[1])])
       ]    
   petri_net = PetriNet(ts,ps)
   petri_net.run()
   t = input("Ban co muon xuat file anh ket qua khong (Y: yes, cac ky tu khac tu dong la No): ")
   if t == "Y":
      petri_net.export("SolvingProblem_3")            # Trich xuat file anh co ten nhu tren
def SolvingPro_4():
   return True


if __name__ == "__main__":
   
   while True:
      print("Chon van bai toan can giai quyet (nhap 1, 2, 3,4 hoac 5): ")
      print("1: Bai toan 1")
      print("2: Bai toan 2")
      print("3: Bai toan 3")
      print("4: Bai toan 4")
      print("5: Thoat")
      print("Nhap: ", end ='')
      try:
         t = int(input())
      except ValueError:
         print("So khong hop le! Vui long nhap lai...")
         continue
      if t == 1:
         SolvingPro_1()
      elif t == 2:
         SolvingPro_2()
      elif t == 3:
         SolvingPro_3()
      elif t == 4:
         SolvingPro_4()
      elif t == 5:
         break
      else:
         print("Gia tri phai la so nguyen trong doan [1,5]. Vui long nhap lai!!!")

