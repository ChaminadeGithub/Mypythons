ma_famille = {"Premier_enfant": "ABIDE", "Deuxieme_enfant":"JEAN", "Troisieme_enfant":"FRANCK", "Quatrieme_enfant":"CHAMINADE", "Cinquieme_enfant":"JOVANIE", "Sixieme_enfant":"Adeline"}

find = input("Entrer votre prenom :")

for un_nom in ma_famille:

    match un_nom:

		case "ABIDE":
			un_nom = "ABIDE"
			print(f"{un_nom} est le premier enfant de la famille")
			print(f"{Premir_enfant} est la grande soeur")

			continue find

		case "JEAN":
			un_nom = "JEAN"
			print(f"{un_nom} est le Deuxieme_enfant de la famille")
			print(f"{Deuxiem_enfant} est le premier grand frere")

			continue find

		case "FRANCK":
			un_nom = "FRANCK"
			print(f"{un_nom} est le Troisieme enfant de la famille")
			print(f"{Troisieme_enfant} est le deuxieme grand frere")

			continue find


		case "CHAMINADE":
			print(f"{un_nom} est le quatrieme enfant de la famille")
			print(f"{Quatrieme_enfant} est le troisieme grand frere")

			continue find

		case "JOVANIE":
			print(f"{un_nom} est le cinquieme enfant de la famille")
			pprint(f"{Cinquieme_enfant} est l'avant dernier de la famille")

			continue(find)

		case "Adeline":
			print(f"{un_nom} est le sixieme enfant de la famille")
			pprint(f"{Sixieme_enfant} est le dernier de la famille et la benjamine")

			continue find


		case "":
			print("Voudez entrer un prenom")

			continue find

