# rs_projekt

#Lost & Found aplikacija sustav s nagradama

Sustav omogućuje decentraliziranu objavu, pretragu i nagrađivanje pronalaska izgubljenih predmeta ili ljubimaca koristeći blockchain tehnologiju kao posrednika od povjerenja.
Osnovna ideja sustava je rješavanje problema nesigurnosti pri isplati nagrade: nalaznik ima garanciju da je nagrada osigurana (rezervirana u Smart Contractu), dok vlasnik ima garanciju da će sredstva biti isplaćena tek nakon potvrde o pronalasku. Sustav funkcionira bez centralnog autoriteta, čime se eliminiraju provizije i omogućuje globalna dostupnost mreže "tragača".

# Tok rada sustava:

##### Objava oglasa (Bounty Creation) – Korisnik koji je izgubio predmet unosi detaljan opis i lokaciju gubitka, te uplaćuje iznos nagrade (npr. u ETH ili tokenima) direktno u Smart Contract.

##### Zaključavanje sredstava (Escrow) – Smart Contract sigurno čuva sredstva na blockchainu. Nagrada je "vidljiva" svima, što služi kao motivacija nalaznicima, ali nitko (pa ni vlasnik) ne može povući sredstva dok je potraga aktivna.

##### Prijava pronalaska (Claim) – Osoba koja pronađe predmet putem aplikacije šalje dokaz o pronalasku (npr. fotografiju ili kriptografski hash dokaza). Sustav obavještava vlasnika o potencijalnom pronalasku.

##### Verifikacija i primopredaja – Vlasnik provjerava dokaz. U trenutku primopredaje predmeta, vlasnik potvrđuje identitet nalaznika (npr. skeniranjem unikatnog QR koda nalaznika).

##### Automatska isplata – Nakon potvrde vlasnika, Smart Contract automatski i trenutno prebacuje zaključana sredstva na novčanik nalaznika. Ako se predmet ne pronađe u određenom roku, vlasnik može povući sredstva natrag.

#Prva ideja

Sustav omogućuje unos, pohranu i verifikaciju dokumenata (npr. putovnice, osobne iskaznice, potvrde) pomoću blockchain tehnologije.
Kod unosa dokumenta provjerava se OIB korisnika, a podaci se kriptografski potpisuju i spremaju u blockchain.
Kada osoba, primjerice, dođe na granicu, sustav omogućuje provjeru autentičnosti dokumenta uspoređujući hash dokumenta s onim koji je zapisan na blockchainu, čime se potvrđuje da dokument nije mijenjan i da je važeći.
Korisnik također može preuzeti svoj dokument u PDF obliku ili vidjeti status verifikacije.

# Tok rada sustava:

##### Unos podataka – korisnik ili službenik unosi podatke o osobi i dokumentu (OIB, ime, vrsta dokumenta).

##### Verifikacija OIB-a – sustav provjerava ispravnost OIB-a (algoritamski ili preko API-ja).

##### Blockchain zapis (smart contract) – hash dokumenta i osnovni metapodaci spremaju se u blockchain (npr. Ethereum testnet ili lokalni blockchain).

##### Generiranje PDF-a – dokument se sprema kao PDF koji sadrži QR kod (QR vodi do blockchain zapisa).

##### Verifikacija – na granici, službenik skenira QR kod ili upiše ID, a sustav provjerava u blockchainu je li dokument autentičan i važeći.



Update sa sata: 3.11.2025:
QR osobna , qr kod(koji vodi do E-osobne) se skenira i netko može potvrditi Vaš identitet uživo kada Vas vidi.



