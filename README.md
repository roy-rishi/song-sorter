# song-sorter
Play a sorting game with your favorite artist!
An artist's discography is gathered from an inputted artist URI or URL (as can be be located from the share dialog in the Spotify application).
The ability to filter by playlist is provided.
 
## install
### dependencies
* `python3 -m pip install spotipy==2.23.0`

### credentials
write `cred.py` to the project directory according to the following template 
```py
client_id="your_client_id"
client_secret="your_client_secret"
redirect_url="your_redirect_url"
```

## example
```bash
➜ song-sorter $ python3 main.py                       
 
enter artist uri: spotify:artist:163tK9Wjr9P9DmM0AVK7lm 
 
gathering tracks from albums... 
 
Te Ao Mārama 
Supercut (El-P Remix) 
Homemade Dynamite (Feat. Khalid, Post Malone & SZA) [REMIX] 
Green Light (Chromeo Remix) 
Flicker (Kanye West Rework) [From The Hunger Games: Mockingjay Part 1] 
Yellow Flicker Beat (From The Hunger Games: Mockingjay Part 1) 
Tennis Court (Flume Remix) 
No Better 
The Love Club EP 
Bravado (Fffrrannno Remix) 
Tennis Court 
Live In Concert 
Solar Power (Deluxe Edition) 
Solar Power 
Melodrama 
Pure Heroine 
 
71 entries 
{'ranking': 1000, 'name': 'Hard Feelings/Loveless', 'album': 'Melodrama'} 
{'ranking': 1000, 'name': 'The Path', 'album': 'Solar Power (Deluxe Edition)'} 
{'ranking': 1000, 'name': 'Homemade Dynamite (Feat. Khalid, Post Malone & SZA) - REMIX', 'album': 'Homemade Dynamite (Feat. Khalid, Post Malone & SZA) [REMIX]'}
{'ranking': 1000, 'name': 'Leader of a New Regime', 'album': 'Solar Power'} 
{'ranking': 1000, 'name': 'Bravado', 'album': 'The Love Club EP'} 
{'ranking': 1000, 'name': 'Oceanic Feeling', 'album': 'Solar Power'} 
{'ranking': 1000, 'name': 'Green Light - Chromeo Remix', 'album': 'Green Light (Chromeo Remix)'} 
{'ranking': 1000, 'name': 'Liability (Reprise)', 'album': 'Melodrama'} 
{'ranking': 1000, 'name': 'Royals', 'album': 'Pure Heroine'} 
{'ranking': 1000, 'name': 'Stoned at the Nail Salon', 'album': 'Solar Power (Deluxe Edition)'} 
{'ranking': 1000, 'name': 'Royals - Live In Concert 2013', 'album': 'Live In Concert'} 
{'ranking': 1000, 'name': 'Ribs', 'album': 'Pure Heroine'} 
{'ranking': 1000, 'name': 'Writer In The Dark', 'album': 'Melodrama'} 
{'ranking': 1000, 'name': 'Biting Down', 'album': 'The Love Club EP'} 
{'ranking': 1000, 'name': 'Swingin Party', 'album': 'Tennis Court'} 
{'ranking': 1000, 'name': 'Buzzcut Season', 'album': 'Pure Heroine'} 
{'ranking': 1000, 'name': 'Hold No Grudge - Bonus Track', 'album': 'Solar Power (Deluxe Edition)'} 
{'ranking': 1000, 'name': 'Hua Pirau / Fallen Fruit', 'album': 'Te Ao Mārama'} 
{'ranking': 1000, 'name': 'Big Star', 'album': 'Solar Power'} 
{'ranking': 1000, 'name': 'Leader of a New Regime', 'album': 'Solar Power (Deluxe Edition)'} 
{'ranking': 1000, 'name': 'Stoned at the Nail Salon', 'album': 'Solar Power'} 
{'ranking': 1000, 'name': 'Fallen Fruit', 'album': 'Solar Power'} 
{'ranking': 1000, 'name': 'No Better', 'album': 'No Better'} 
{'ranking': 1000, 'name': 'California', 'album': 'Solar Power'} 
{'ranking': 1000, 'name': 'Oceanic Feeling', 'album': 'Solar Power (Deluxe Edition)'} 
{'ranking': 1000, 'name': 'Yellow Flicker Beat', 'album': 'Yellow Flicker Beat (From The Hunger Games: Mockingjay Part 1)'} 
{'ranking': 1000, 'name': 'Tennis Court - Flume Remix', 'album': 'Tennis Court (Flume Remix)'} 
{'ranking': 1000, 'name': 'Buzzcut Season - Live In Concert 2013', 'album': 'Live In Concert'} 
{'ranking': 1000, 'name': 'Solar Power', 'album': 'Solar Power (Deluxe Edition)'} 
{'ranking': 1000, 'name': 'Helen of Troy - Bonus Track', 'album': 'Solar Power (Deluxe Edition)'} 
{'ranking': 1000, 'name': 'Big Star', 'album': 'Solar Power (Deluxe Edition)'} 
{'ranking': 1000, 'name': 'Glory And Gore', 'album': 'Pure Heroine'} 
{'ranking': 1000, 'name': 'Perfect Places', 'album': 'Melodrama'} 
{'ranking': 1000, 'name': 'Tennis Court', 'album': 'Pure Heroine'} 
{'ranking': 1000, 'name': 'Dominoes', 'album': 'Solar Power (Deluxe Edition)'} 
{'ranking': 1000, 'name': 'White Teeth Teens', 'album': 'Pure Heroine'} 
{'ranking': 1000, 'name': 'Hine-i-te-Awatea / Oceanic Feeling', 'album': 'Te Ao Mārama'} 
{'ranking': 1000, 'name': 'California', 'album': 'Solar Power (Deluxe Edition)'} 
{'ranking': 1000, 'name': 'Te Ara Tika / The Path', 'album': 'Te Ao Mārama'} 
{'ranking': 1000, 'name': 'The Louvre', 'album': 'Melodrama'} 
{'ranking': 1000, 'name': 'Royals', 'album': 'The Love Club EP'} 
{'ranking': 1000, 'name': 'Solar Power', 'album': 'Solar Power'} 
{'ranking': 1000, 'name': 'Liability', 'album': 'Melodrama'} 
{'ranking': 1000, 'name': '400 Lux - Live In Concert 2013', 'album': 'Live In Concert'} 
{'ranking': 1000, 'name': 'Supercut - El-P Remix', 'album': 'Supercut (El-P Remix)'} 
{'ranking': 1000, 'name': 'Flicker (Kanye West Rework)', 'album': 'Flicker (Kanye West Rework) [From The Hunger Games: Mockingjay Part 1]'} 
{'ranking': 1000, 'name': 'The Path', 'album': 'Solar Power'} 
{'ranking': 1000, 'name': 'Homemade Dynamite', 'album': 'Melodrama'} 
{'ranking': 1000, 'name': 'Green Light', 'album': 'Melodrama'} 
{'ranking': 1000, 'name': "Secrets from a Girl (Who's Seen it All)", 'album': 'Solar Power'} 
{'ranking': 1000, 'name': 'Fallen Fruit', 'album': 'Solar Power (Deluxe Edition)'} 
{'ranking': 1000, 'name': 'Still Sane', 'album': 'Pure Heroine'} 
{'ranking': 1000, 'name': 'Swingin Party - Live In Concert 2013', 'album': 'Live In Concert'} 
{'ranking': 1000, 'name': 'The Love Club', 'album': 'The Love Club EP'} 
{'ranking': 1000, 'name': 'Million Dollar Bills', 'album': 'The Love Club EP'} 
{'ranking': 1000, 'name': 'Tennis Court', 'album': 'Tennis Court'} 
{'ranking': 1000, 'name': 'The Man with the Axe', 'album': 'Solar Power'} 
{'ranking': 1000, 'name': 'Supercut', 'album': 'Melodrama'} 
{'ranking': 1000, 'name': 'Mata Kohore / Stoned at the Nail Salon', 'album': 'Te Ao Mārama'} 
{'ranking': 1000, 'name': 'Mood Ring', 'album': 'Solar Power (Deluxe Edition)'} 
{'ranking': 1000, 'name': "Secrets from a Girl (Who's Seen it All)", 'album': 'Solar Power (Deluxe Edition)'} 
{'ranking': 1000, 'name': 'Bravado - Fffrrannno Remix', 'album': 'Bravado (Fffrrannno Remix)'} 
{'ranking': 1000, 'name': 'Mood Ring', 'album': 'Solar Power'} 
{'ranking': 1000, 'name': 'Team', 'album': 'Pure Heroine'} 
{'ranking': 1000, 'name': 'Te Ao Mārama / Solar Power', 'album': 'Te Ao Mārama'} 
{'ranking': 1000, 'name': 'A World Alone', 'album': 'Pure Heroine'} 
{'ranking': 1000, 'name': '400 Lux', 'album': 'Pure Heroine'} 
{'ranking': 1000, 'name': 'Sober', 'album': 'Melodrama'} 
{'ranking': 1000, 'name': 'The Man with the Axe', 'album': 'Solar Power (Deluxe Edition)'} 
{'ranking': 1000, 'name': 'Sober II (Melodrama)', 'album': 'Melodrama'} 
{'ranking': 1000, 'name': 'Dominoes', 'album': 'Solar Power'} 
 
Albums 
1. Melodrama 
2. Solar Power (Deluxe Edition) 
3. Homemade Dynamite (Feat. Khalid, Post Malone & SZA) [REMIX] 
4. Solar Power 
5. The Love Club EP 
6. Green Light (Chromeo Remix) 
7. Pure Heroine 
8. Live In Concert 
9. Tennis Court 
10. Te Ao Mārama 
11. No Better 
12. Yellow Flicker Beat (From The Hunger Games: Mockingjay Part 1) 
13. Tennis Court (Flume Remix) 
14. Supercut (El-P Remix) 
15. Flicker (Kanye West Rework) [From The Hunger Games: Mockingjay Part 1] 
16. Bravado (Fffrrannno Remix) 
 
enter comma-separate indexes of the album(s) to include: 1 
 
including ['Melodrama'] 
 
11 entries 
{'ranking': 1000, 'name': 'Hard Feelings/Loveless', 'album': 'Melodrama'} 
{'ranking': 1000, 'name': 'Liability (Reprise)', 'album': 'Melodrama'} 
{'ranking': 1000, 'name': 'Writer In The Dark', 'album': 'Melodrama'} 
{'ranking': 1000, 'name': 'Perfect Places', 'album': 'Melodrama'} 
{'ranking': 1000, 'name': 'The Louvre', 'album': 'Melodrama'} 
{'ranking': 1000, 'name': 'Liability', 'album': 'Melodrama'} 
{'ranking': 1000, 'name': 'Homemade Dynamite', 'album': 'Melodrama'} 
{'ranking': 1000, 'name': 'Green Light', 'album': 'Melodrama'} 
{'ranking': 1000, 'name': 'Supercut', 'album': 'Melodrama'} 
{'ranking': 1000, 'name': 'Sober', 'album': 'Melodrama'} 
{'ranking': 1000, 'name': 'Sober II (Melodrama)', 'album': 'Melodrama'} 
 
 
Start Sorting Songs! 
"1": Song 1 Wins   "2": Song 2 Wins   "a": Abort 
 
Battle 1 
1. Hard Feelings/Loveless  -  Melodrama 
2. Liability (Reprise)  -  Melodrama 
1 or 2: 2 
 
Battle 2 
1. Supercut  -  Melodrama 
2. The Louvre  -  Melodrama 
1 or 2: 2 
 
Battle 3 
1. Green Light  -  Melodrama 
2. Liability  -  Melodrama 
1 or 2: 1 
 
Battle 4 
1. Writer In The Dark  -  Melodrama 
2. Liability  -  Melodrama 
1 or 2: a 
 
aborting... 
 
 
Detailed results are as follows 
 
11.	Liability  -  Melodrama 
	  984.3528000084657 
10.	Hard Feelings/Loveless  -  Melodrama 
	  985.0 
9.	Supercut  -  Melodrama 
	  985.0 
8.	Homemade Dynamite  -  Melodrama 
	  1000 
7.	Perfect Places  -  Melodrama 
	  1000 
6.	Sober  -  Melodrama 
	  1000 
5.	Sober II (Melodrama)  -  Melodrama 
	  1000 
4.	Writer In The Dark  -  Melodrama 
	  1000 
3.	Green Light  -  Melodrama 
	  1015.0 
2.	Liability (Reprise)  -  Melodrama 
	  1015.6471999915343 
1.	The Louvre  -  Melodrama 
	  1015.6471999915343 
 
 
Your results are as follows 
 
11.	Liability 
10.	Hard Feelings/Loveless 
9.	Supercut 
8.	Homemade Dynamite 
7.	Perfect Places 
6.	Sober 
5.	Sober II (Melodrama) 
4.	Writer In The Dark 
3.	Green Light 
2.	Liability (Reprise) 
1.	The Louvre 
➜ song-sorter $  
```
