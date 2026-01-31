// passtr - a simple static analysis warm up exercise
// Copyright 2024 Tero Karvinen https://TeroKarvinen.com

#include <stdio.h>
#include <string.h>

int main() {
	char password[20];

	// puskuri oikealle salasanalle, joka rakennetaan ajon aikana
	char expected[20];

	// alustetaan merkkijono tyhjäksi ennen strcat-kutsuja
	expected[0] = '\0';

	// salasana jaetaan kahden merkin paloihin, jotta koko salasana ei esiinny binäärissä yhtenäisenä merkkijonona
	strcat(expected, "sa");
	strcat(expected, "la");
	strcat(expected, "-h");
	strcat(expected, "ak");
	strcat(expected, "ke");
	strcat(expected, "ri");
	strcat(expected, "-3");
	strcat(expected, "21");
	
	printf("What's the password?\n");
	scanf("%19s", password);
	// verrataan käyttäjän syötettä ajon aikana rakennettuun salasanaan
	if (0 == strcmp(password, expected)) {
		printf("Yes! That's the password. FLAG{Tero-d75ee66af0a68663f15539ec0f46e3b1}\n");
	} else {
		printf("Sorry, no bonus.\n");
	}
	return 0;
}
