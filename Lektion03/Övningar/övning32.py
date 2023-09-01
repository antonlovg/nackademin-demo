namn = input("Ange ditt namn: ")
ålder = int(input("Ange din ålder: "))
print("-------")

sömnbehov = {1:14, 2:13, 3:12, 4:11.5, 5:11, 6:11, 7:10.5, 8:10, 9:10, 10:10, 11:9.5, 12:9, 13:9, 14:9, 15:9, 16:8.5}
sömntimmar = sömnbehov.get(ålder, 8)
print(f"Hallå {namn}! Enligt vårdguidens rekommendationer behöver individer i din ålder ({ålder} år) sova minst {sömntimmar} timmar." )
