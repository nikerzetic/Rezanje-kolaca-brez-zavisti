igralec_1.razrezi(kolac)

igralec_2_stori_nic = igralec_2.nic_ali_oznaci_2()

if igralec_2_stori_nic:
	igralec_3.izberi_kos(kolac)
	igralec_2.izberi_kos(kolac)
	igralec_1.vzemi(preostali_kos(kolac)
	
else:
	igralec_3_stori_nic = igralec_3.nica_ali_oznaci_2()
	if igralec_3_stori_nic:
		igralec_2.izberi_kos(kolac)
		igralec_3.izberi_kos(kolac)
		igralec_1.vzemi(preostali_kos(kolac))
	else:
		igralec_1.izberi_kos(oznacil_2(kolac) & oznacil_2(kolac))
		nov_kolac(kolac)
		razrezi_in_izbeeri(nov_kolac, igralec_2, igralec_3)
