def abs(n):
	if n >= 0:
		return n
	elif n < 0:
		return n * (-1)
def support(a,b):
	if a == b:
		return 0
	else:
		return 100
ASHE = {
	"Player_avg" : 0,
	"Name" : "Ashe",
    "Laning" : 33,
    "Kiting" : 0,
    "Support1" : 1,
    "Dodgeing" : 100,
    "TeamFighting" : 50,
    "Support2" : 2,
    "Positioning" : 25,
    "Dueling" : 33,
    "Landing" : 33,
    "Support3" : 3,
    "Tag" : "The Frost Archer",
	"LANING" : "Ashe is very versatile during the laning phase. Her relatively long range and E: Hawkshot allows the player to safely farm, while her Q: Ranger's Focus and R: Enchanted Crystal Arrow gives her amazing kill potential.",
	"TEAMFIGHT" : "The player will find Ashe to be versatile during teamfights as well. Her R: Enchanted Crystal Arrow can initiate teamfights, her W: Volley can be used as a poke before teamfights, and her Q: Ranger's Focus melts enemy frontlines.",
	"DUELING" : "Ashe is not for the hardcore duelist. Although her R: Enchanted Crystal Arrow may win her the 1v1, there are much better ADC duelists out there, especially considering her Q: Ranger's Focus requires set-up time. Therefore, Ashe is great for those that only seek to occassionally duel when the opportunity presents itself.",
	"MECHANICS" : "Due to her immobility, Ashe reaches her potential when the player has a good sense of positioning and prediction against enemy skillshots. On the other hand, when kiting tanks, her passive slow helps her immensely, allowing her to be effective even in the hands of a player who has not mastered kiting.",
	}

CAITLYN = {
	"Player_avg" : 0,
	"Name" : "Caitlyn",
    "Laning" : 67,
    "Kiting" : 0,
    "Support1" : 1,
    "Dodgeing" : 0,
    "TeamFighting" : 25,
    "Support2" : 2,
    "Positioning" : 50,
    "Dueling" : 67,
    "Landing" : 0,
    "Support3" : 3,
    "Tag" : "The Sheriff of Piltover",	
	"LANING" : "Aggressive and passive players alike will appreciate Caitlyn's long range auto-attacks, allowing her to easily harass enemies and seriously crippling enemy laners if Caitlyn is resourceful with her passive, made even easier after getting a Runaan's Hurricane. Caitlyn's E: Yordle Snap Trap gives bush control as well as deter ganks. She can easily push the lane and siege the enemy laner under their tower using Q: Piltover Peacemaker, or, if behind, safely farm from a distance.",
	"TEAMFIGHT" : "Caitlyn's contribution to teamfights centers heavily on items and levels, making her a great choice for players lacking in \"MECHANICS\" :. Her Q: Piltover Peacemaker and R: Ace in the Hole are easy to land and bring superb damage in early teamfights, while her passive, W: Yordle Snap Trap, and E: 90 Caliber Net scale very well into late game fights.",
	"DUELING" : "Caitlyn is a decent duelist, but shines more in skirmishes and teamfights. Landing a full combo (W-passive auto-E-auto-Q-R) is a surprisingly high amount of damage, and can 0 to 100 squishies if ahead, allowing the player the choice of whether to engage the 1v1 or disengae with her E: 90 Caliber Net.",
	"MECHANICS" : "Caitlyn does not require a high skill floor in movement and skillshot \"MECHANICS\" :. Her skillshots are easy to land, and her range lets her stay safe where a large portion of enemy skillshots will not reach her. Due to her range and mobility, the player will also not have to worry too much on auto-attach \"MECHANICS\" :. Of course, with better \"MECHANICS\" :, the more effective Caitlyn will be.",
    }

CORKI = {
	"Player_avg" : 0,
	"Name" : "Corki",
    "Laning" : 33,
    "Kiting" : 50,
    "Support1" : 2,
    "Dodgeing" : 67,
    "TeamFighting" : 25,
    "Support2" : 1,
    "Positioning" : 50,
    "Dueling" : 33,
    "Landing" : 100,
    "Support3" : 2,
    "Tag" : "The Daring Bombardier",
    "LANING" : "Corki shines in the hands of a player who likes to pressure enemies and trade. After getting a sheen item, Corki trades well against the average ADC, and can keep the pressure on the enemy laners by pushing to tower and sieging them post-level 6. His Q: Phosphorus Bomb and R: Missile Barrage clears waves fast in case the player is behind.",
	"TEAMFIGHT" : "Players who do not enjoy the intensity of late-game teamfights should make full use of Corki's R: Missile Barrage, one of the most amazing ADC abilities for poking. Players who do not always have the best positioning can use Corki's W: Valkyrie to reposition or get away if dived on.",
	"DUELING" : "For players that consistently land skillshots, Corki can put out respectable damage in a 1v1, as the player can rotate through all of his abilities and proc Sheen on cooldown. But should the player choose, Corki would do good, if not better, with his teammates where he excels in poking down the enemy.",
	"MECHANICS" : "To play Corki effectively, the player should have excellent skillshot-landing abilities, as well as general knowledge of when to poke, engage, or disengage. Players with mediocre dodging and positioning skills should find Corki to be forgiving thanks to his W: Valkyrie. ",
	}

DRAVEN = {
	"Player_avg" : 0,
	"Name" : "Draven",
    "Laning" : 100,
    "Kiting" : 100,
    "Support1" : 2,
    "Dodgeing" : 100,
    "TeamFighting" : 75,
    "Support2" : 1,
    "Positioning" : 0,
    "Dueling" : 100,
    "Landing" : 33,
    "Support3" : 2,
    "Tag" : "The Glorious Executioner",
	"LANING" : "Draven shines in the hands of an aggressive laner. His attack steroid in Q: Spinning Axe and W: Blood Rush puts him on top in literally every trade, especially if coupled with poke or all-in supports. Thanks to the passive gold from his passive, coming out ahead during the laning phase transitions superbly into teamfighting.",
	"TEAMFIGHT" : "Draven demands the player to be on top of his game during a teamfight. His Q: Spinning Axe requires the player to know where all enemies are at all times, and the player must be alert for opportunities to use R: Whirling Death.",
	"DUELING" : "The dueling player will love Draven's damage output. His mobility with W: Blood Rush and E: Stand Aside allows him to tangle with tanks and squishies alike. To an enemy carry, Draven's auto-attacks might as well by burst spells, and tanks literally melt if they do not crowd-control Draven down.",
	"MECHANICS" : "Draven is not for the faint of heart. Few possess the mechanical prowess and dedication needed to bring out Draven's potential. However, players with pinpoint accuracy, amazing positioning, and high APM will be duly rewarded in the League of Draven.",
	}

EZREAL = {
	"Player_avg" : 0,
	"Name" : "Ezreal",
    "Laning" : 33,
    "Kiting" : 75,
    "Support1" : 2,
    "Dodgeing" : 67,
    "TeamFighting" : 75,
    "Support2" : 1,
    "Positioning" : 100,
    "Dueling" : 100,
    "Landing" : 67,
    "Support3" : 2,
    "Tag" : "The Prodigal Explorer",
	"LANING" : "Depending on the player's playstyle or the aggressiveness of the support, Ezreal can be great in the lands of a passive laner, where he farms for 2 or 3 item power spike, or in the hands of an aggressive laner, poking down the enemy with Q: Mystic Shot, then going in for the kill with E: Arcane Shift.",
	"TEAMFIGHT" : "Players who enjoy the chaos of teamfights will find Ezreal to be especially fun as his mobility is arguably the highest among marksmen. His R: Trueshot Barrage and W: Essence Flux can and should hit multiple enemies, while his Q: Mystic Shot is an amazing poke tool prior to teamfighting.",
	"DUELING" : "Playing with a next level Ezreal is truly a sight to behold. Players with pinpoint accuracy in landing skillshots and knowing enemy cooldowns will be rewarded with the above-average dueling potential that Ezreal is capable of. Hitting a full combo (Q-auto-W-auto-E-auto-Q-auto-R) will likely 0-100 squishies.",
	"MECHANICS" : "If you love juking enemies and hitting them with skillshots, you will love Ezreal. To bring out the potential of Ezreal, the player must have a great sense of positioning and skillshot landing, as well as predicting enemy skillshots and dashes.",
	}

JHIN = {
	"Player_avg" : 0,
	"Name" : "Jhin",
    "Laning" : 0,
    "Kiting" : 50,
    "Support1" : 2,
    "Dodgeing" : 67,
    "TeamFighting" : 50,
    "Support2" : 1,
    "Positioning" : 0,
    "Dueling" : 0,
    "Landing" : 100,
    "Support3" : 2,
    "Tag" : "The Virtuoso",	
	"LANING" : "Jhin's laning is meant for the safe and calculating player. His abilities in the early game does not have the kill potential that other marksmen have therefore, the Jhin player will tend to favor farming until a 2 item power spike by going Infinity Edge then Rapid Fire Cannon. In addition, Jhin's passive and Q: Dancing Grenade provides the player with minion-executing ease.",
	"TEAMFIGHT" : "For players that value siege and pick potential rather than an all-out brawl, Jhin is the champion for you. With fantastic burst damage coming from his passive and long-range pick potential from his W: Deadly Flouish and R: Curtain Calls, Jhin excels in the hands of someone who strategizes rotations and objectives. While Jhin can provide reliable damage output during a teamfight, his immobility makes him an easy prey for assassins and supertanks.",
	"DUELING" : "Jhin players will typically favor skirmishes and catches rather than duels. Although his passive provides fantastic burst damage if the last shot lands, bruisers, tanks, or anyone that survives his burst can catch Jhin off guard as he is reloading.",
	"MECHANICS" : "Jhin's immobility requires the player to have great positioning and skillshot dodging skills. However, the APM and movement \"MECHANICS\" : of the player does not need to be exceptional, as his passive and low rate of fire helps players who might otherwise have trouble with kiting, especially once Jhin acquires high critical chance.",
	}

JINX = {
	"Player_avg" : 0,
	"Name" : "Jinx",
    "Laning" : 67,
    "Kiting" : 50,
    "Support1" : 2,
    "Dodgeing" : 100,
    "TeamFighting" : 75,
    "Support2" : 1,
    "Positioning" : 25,
    "Dueling" : 33,
    "Landing" : 67,
    "Support3" : 2,
    "Tag" : "The Loose Cannon",	
	"LANING" : "Jinx is an extremely versatile and powerful laner. Players can choose to harass with W: Zap and Q: Switcheroo, all-in with E: Flame Chompers and R: Super Mega Death Rocket, or farm from a distance with Q: Switcheroo.",
	"TEAMFIGHT" : "Despite having no dashes or escapes, Jinx brings damage in spades during teamfights, which is particularly good considering her reset passive. Players that utilize Jinx's many utility abilities before and during a teamfight will bring out her full potential, topping damage meters and hard carrying late game.",
	"DUELING" : "Jinx offers plenty of damage for the dueling-happy, but is severely limited by her immobility. While Q: Switcheroo and R: Super Mega Death Rocket are amazing dueling abilities, she shines more in the hands of someone who likes skirmishes and teamfights.",
	"MECHANICS" : "Due to her immobility, Jinx players require amazing skillshot dodging, skillshot landing, and teamfight positioning skills. Fortunately, with good placement of W: Zap and E: Flame Chompers, enemies can be locked taken down before getting too close to her, so a player with mediocre kiting skills should find respite in her ability to slow down all by the most dash-iest of divers.",
	}

KALISTA = {
	"Player_avg" : 0,
	"Name" : "Kalista",
    "Laning" : 0,
    "Kiting" : 100,
    "Support1" : 3,
    "Dodgeing" : 0,
    "TeamFighting" : 75,
    "Support2" : 3,
    "Positioning" : 100,
    "Dueling" : 75,
    "Landing" : 0,
    "Support3" : 1,
    "Tag" : "The Spear of Vengeance",	
	"LANING" : "Players who favor farming over aggressively pursuing enemy laners will find Kalista's E: Rend to be very useful in executing minions. While her W: Sentinel allows her and her support to put out percentage-health damage, Kalista will typically not ranked it all the way up during the laning phase. In other words, Kalista players will tend to farm for a Blade of the Ruined King/Runaan's Hurricane and level 9+ power spike rather than constant pressure.",
	"TEAMFIGHT" : "Kalista is for the player who enjoy dominating a teamfight, but may or may not have the \"MECHANICS\" : to always be on point. Kalista's passive greatly enhances the player's ability to dodge skillshot because of the erratic nature of her jumps. Kalista is also arguably the best tank kiter in late game fights, so a player that enjoys a mobile kiting style of gameplay will maximize Kalista's potential.",
	"DUELING" : "Even though Kalista's W: Sentinel and R: Fate's Call requires the presence of her Oathsworn, she still remains a decent duelist after getting her two core attack speed items and boots. Not only do enemies have a terrible time predicting her movements (imagine fighting a Kalista as an Ezreal), but her R: Rend can be a powerful execute. She is not as effective against auto-attack champions like Vayne, but the dueling-inclined will nevertheless find Kalista to be fit for most 1v1s.",
	"MECHANICS" : "Mastering Kalista means understanding kiting \"MECHANICS\" : and optimal range - when to jump forward, jump sideways, or jump back. Because of the range on her Q: Pierce and her dashing playstyle, Kalista will be effective even if the player does not always have the best initial positioning. However, high APM and clicking accuracy is a must-have for playing this vengeful spirit.",
	}

KOG_MAW = {
	"Player_avg" : 0,
	"Name" : "Kog'Maw",
    "Laning" : 0,
    "Kiting" : 100,
    "Support1" : 1,
    "Dodgeing" : 100,
    "TeamFighting" : 100,
    "Support2" : 2,
    "Positioning" : 0,
    "Dueling" : 0,
    "Landing" : 67,
    "Support3" : 3,  
    "Tag" : "The Mouth of the Abyss",	
	"LANING" : "If your middle name is farmer, then Kog Maw is for you. Being such a late game monster, he relies on levels in his W: Bio-Arcane Barrage and a special build path consisting of Guinsoo's Rageblade and Runaan's Hurricane to be effective. Hence, Kog Maw is perfect for your 200+ farm end game fantasy, but not so much for that dominant lane.",
	"TEAMFIGHT" : "What can one say about Kog Maw's teamfighting power that hasn't already been said by everyone else. If you enjoy carrying the crap out of end game teamfights, look no further. Itemizing for attack speed and on-hit effects makes his W: Bio-Arcane Barrage an absolute tank shredder, and his R: Living Artillery is a long-range execute. His immobility, however, makes him easy prey for assassins, and thus requires decent understanding of good positioning to play well.",
	"DUELING" : "Before level 6, Kog Maw will typically lose every trade. Although by late game Kog Maw can put out enough damage to DPS down most enemies before they kill him, there's a high chance Kog Maw will die as well. Therefore, players who value teamfighting and skirmishes will certainly enjoy more success with the Kog.",
	"MECHANICS" : "While Kog Maw can certainly be played as a stationary turret sitting behind a strong front line, players with high APM and kiting abilities will squeeze more out of this void beast. In addition, the ideal Kog player will also have notable skillshot landing and dodging abilities stemming from his lack of escapes and pinpoint R:Living Artillery accuracy.",
	}

LUCIAN = {
	"Player_avg" : 0,
	"Name" : "Lucian",
    "Laning" : 100,
    "Kiting" : 75,
    "Support1" : 3,
    "Dodgeing" : 33,
    "TeamFighting" : 50,
    "Support2" : 3,
    "Positioning" : 100,
    "Dueling" : 100,
    "Landing" : 0,
    "Support3" : 1,
    "Tag" : "The Purifier",
	"LANING" : "Lucian's high burst output from his passive, even pre-level 6, is perfect for the aggressive player who loves to bully the enemies under their tower and continue to harass them with Q: Piercing Light and W: Ardent Blaze. In addition, his R: The Culling has a ridiculous amount of damage and range at level 6, allowing him to go in for the kill even if the enemies are shelled up under tower.",
	"TEAMFIGHT" : "Players who flourish in teamfights will certainly appreciate Lucian's excellent damage in both the early game and scaling into the late game. His only downside, a low auto-attack range, is partially remedied by his exceptional mobility after ranking up his E: Relentless Pursuit.",
	"DUELING" : "Lucian is among the best marksmen duelists. By proccing his passive after every ability in his combo (E-auto-Q-auto-W-auto-E-auto-R), the duel-happy player will love Lucian's ability to 0-100 squishies while having excellent mobility to dodge enemy skillshots.",
	"MECHANICS" : "Lucian's high mobility and long range Q: Piercing Light makes him very forgiving for players that often get caught by hooks. However, Lucian does require the player to have certain prerequisite skillshot landing and kiting skills to be effective. As Lucian, there are few things worse than canceling passive-empowered autos and right-clicking behind the incoming enemy tank.",
	}

MFORTUNE = {
	"Player_avg" : 0,
	"Name" : "Miss Fortune",
    "Laning" : 67,
    "Kiting" : 25,
    "Support1" : 1,
    "Dodgeing" : 67,
    "TeamFighting" : 0,
    "Support2" : 2,
    "Positioning" : 25,
    "Dueling" : 0,
    "Landing" : 67,
    "Support3" : 3,
    "Tag" : "The Bounty Hunter",	
	"LANING" : "Miss Fortune is perfect for players that like to push the wave and win trades in lane. Her passive and Q: Double Up puts up good burst in the early levels, and can be extremely frustrating to play against. When the enemy laner goes up to last-hit a minion, a quick auto-Q-runaway is why Miss Fortune is up there in the lane bullies category.",
	"TEAMFIGHT" : "Players that do not like diving into the fray of a 5v5 teamfight will find solace in Miss Fortune's easy-to-use E: Make It Rain and R: Bullet Time. A fully channeled R: Bullet Time can change the game, as it can easily chunk the health of everyone on the enemy team without Miss Fortune having to auto-attack once. For those that truly seek to avoid teamfighting, Miss Fortune's superb damage output in skirmishes puts her in any pick or rotation comp thanks to her movement speed boost in W: Strut.",
	"DUELING" : "While Miss Fortune can put out a healthy amount of damage in a 1v1, she cannot fully make use of her passive and Q: Double Up. Tanks that get in her face can usually damage her twice and make her W: Strut useless. Thus, Miss Fortune is much better off in the hands of a teamfight or pick comp.",
	"MECHANICS" : "Players with a good understanding of teamfight and skirmish positioning will have a much easier time bringing out Miss Fortune's potential since her Q: Double Up and R: Bullet Time requires a bit of geometry to optimize. Miss Fortune is also good for players that are not the most adept at kiting since her W: Strut and E: Make It Rain will help the player in keeping a distance from the enemy tanks.",
	}

SIVIR = {
	"Player_avg" : 0,
	"Name" : "Sivir",
    "Laning" : 67,
    "Kiting" : 75,
    "Support1" : 1,
    "Dodgeing" : 0,
    "TeamFighting" : 0,
    "Support2" : 2,
    "Positioning" : 75,
    "Dueling" : 33,
    "Landing" : 33,
    "Support3" : 3,
    "Tag" : "The Battle Mistress",	
	"LANING" : "When Sivir pushes lane, she pushes hard. Although she has a short auto-attack range, her Q: Boomerang Blade and W: Ricochet extends her effective range significantly. Post-level 6, Sivir's R: On The Hunt is a great initiator for skirmishes or ganks. Thus, if you lean towards being aggressive in lane, or like to push enemies to tower to harass them to make them miss minions, then Sivir is perfect.",
	"TEAMFIGHT" : "Sivir's R: On The Hunt brings excellent utility when teamfighting, and can be used to either engage or disengage. For players that would rather take objectives than risk it all on a teamfight, Sivir's excellent wave-clearing power and disengage tool makes an amazing choice for players that prefer a pick or split push comp.",
	"DUELING" : "Sivir's kit offers many tools for players that love to duel. Her E: Spell Shield is vital for blocking key damaging attacks or crowd control, while her passive allows her to easily kite or dodge. That being said, Sivir fares much better when used in skirmishes or small teamfights, where she can make full use of her area-of-effect W: Ricochet and R: On The Hunt.",
	"MECHANICS" : "Rather than requiring precise positioning or skillshot dodging \"MECHANICS\" :, the ideal Sivir player has an uncanny timing on using Sivir's E: Spellshield. Her low auto-attack range also means the player must be keen to kiting, although Sivir's passive certainly makes kiting easier for those slightly less mechanically inclined.",
	}

TRISTANA = {
	"Player_avg" : 0,
	"Name" : "Tristana",
    "Laning" : 33,
    "Kiting" : 25,
    "Support1" : 3,
    "Dodgeing" : 67,
    "TeamFighting" : 100,
    "Support2" : 3,
    "Positioning" : 50,
    "Dueling" : 67,
    "Landing" : 0,
    "Support3" : 1,
    "Tag" : "The Yordle Gunner",	
	"LANING" : "Among the late-game carry monsters, Tristana's laning phase is perhaps the most dominant, as her E: Explosive Charge can be used to clear waves while W: Rocket Jump and R: Buster Shot offers serious kill potential when paired with an aggressive support. Therefore, Tristana is perfect for players who love carrying the late game but has the game knowledge and coordination to establish a strong lane.",
	"TEAMFIGHT" : "There's nothing more satisfying than getting multiple resets as Tristana. As the game gets longer, Tristana's range also increases, making her relatively safe as she auto-attacks behind the front lines, or as she decimates towers with Q: Rapid Fire and E: Explosive Charge. ",
	"DUELING" : "What makes Tristana such a monster is that not only is she a late game monster with immense teamfighting potential, she is also a decent duelist as well. Even during the laning phase, a full combo (W-E-auto-auto-auto-R) will 50-0 the enemy ADC. With levels, her Q: Rapid Fire is one of the most powerful attack steroids in the late game, allowing Tristana to itemize for straight damage and critical chance. A dueling-inclined player will have serious kill potential with Tristana.",
	"MECHANICS" : "Tristana's W: Rocket Jump allows her to jump to safety when getting engaged on, and her R: Buster Shot makes her very forgiving for players that aren't the most mechanically adept at kiting. As long as the player has a basic understanding of positioning to make full use of her W: Rocket Jump Reset (and not jumping into the middle of a teamfight), the player will certainly carry the game as the Pocket Rocket.,"
	}

TWITCH = {
	"Player_avg" : 0,
	"Name" : "Twitch",
    "Laning" : 33,
    "Kiting" : 25,
    "Support1" : 2,
    "Dodgeing" : 67,
    "TeamFighting" : 100,
    "Support2" : 1,
    "Positioning" : 25,
    "Dueling" : 67,
    "Landing" : 33,
    "Support3" : 2,
    "Tag" : "The Plague Rat",	
	"LANING" : "Twitch has the option of being played passively in lane, farming for post-level 6 teamfights, or aggressively, stealthing in with Q: Ambush, popping a few autos with W: Venom Cask, then winning the trade with E: Contaminate. With good dodging \"MECHANICS\" :, the Twitch player can come out very far ahead in lane, making his teamfight presence even more threatening.",
	"TEAMFIGHT" : "A post-level 6 Twitch is a threat in any skirmish or teamfight, thanks to the immense amount of damage his R: Rat-Ta-Tat-Tat can put out. He can be played either as a turret behind the front lines, damaging all enemies with a Runaan's Hurricane, or stealth from the flank after key enemy cooldowns have been used. Either way, the Twitch player will look for teamfights.",
	"DUELING" : "Depending on how Twitch is built, his dueling ability can actually be quite high. With Blade of the Ruined King and Youmuu's Ghostblade, a Twitch popping out of Q: Ambush with R: Rat-Ta-Tat-Tat can melt a squishy, provided the Twitch does not get crowd-controlled. Therefore, Twitch offers flexibility to both players who want to be the stealthy assassin, or players that prefer area teamfight damage.",
	"MECHANICS" : "Players that do well with Twitch understand proper teamfight positioning, whether that be the stealthy flank or the Runaan's Hurricane turret. Due to his lack of escapes, enemy skillshot prediction is vital for pumping out damage, since his auto-attack reliant playstyle means less burst and more sustained damage over time survived.",
	}

VARUS = {
	"Player_avg" : 0,
	"Name" : "Varus",
    "Laning" : 100,
    "Kiting" : 75,
    "Support1" : 2,
    "Dodgeing" : 100,
    "TeamFighting" : 25,
    "Support2" : 1,
    "Positioning" : 0,
    "Dueling" : 33,
    "Landing" : 100,
    "Support3" : 2,
    "Tag" : "The Arrow of Retribution",	
	"LANING" : "If the player can consistently land skillshots, there are few laners more dominant than Varus. Not only does W: Blighted Quiver passively give Varus more damage on his auto-attacks, but both his Q: Piercing Arrow and E: Hail of Arrows are bursty long range spells with high base damage. If you favor an aggressive or potential kill lane, Varus should be one of your top choices.",
	"TEAMFIGHT" : "While Varus's R: Chain of Corruption can be a decent initiator during a teamfight, his true strength lies in a poke comp where his Q: Piercing Arrow chunks squishies and his E: Hail of Arrows R: Chain of Corruption can be used as a disengage. ",
	"DUELING" : "Varus is not a great duelist. Despite Varus's abilities are all capable of dishing out massive damage, even against tanks thanks to his W: Blighted Quiver at max rank, his setup time means a burstier carry will take down Varus before he can unleash his full combo (auto-auto-R-auto-auto-auto-W-auto-auto-auto-Q). See how long that was? Stick to poking with Varus, and go in for the kill only when your support or front line engages.",
	"MECHANICS" : "The ideal Varus player will be exceptional at landing skillshots, predicting enemy skillshots, and positioning optimally during a teamfight. Because of his immobility and reliance on executing a long combo, the player will have to master being in the right place and avoid as much damage as possible in order to make full use of his high-damage kit.",
	}

VAYNE = {
	"Player_avg" : 0,
	"Name" : "Vayne",
    "Laning" : 0,
    "Kiting" : 100,
    "Support1" : 3,
    "Dodgeing" : 33,
    "TeamFighting" : 100,
    "Support2" : 3,
    "Positioning" : 75,
    "Dueling" : 100,
    "Landing" : 0,
    "Support3" : 1,
    "Tag" : "The Night Hunter",	
	"LANING" : "There's no simple way to say this: Vayne needs farm and levels. She is notoriously bad in lane, and requires expert knowledge of enemy range and cooldowns to just come out even in lane. But just like the other late-game monster carries, a Vayne that comes out even in lane is ahead. If you like end game fantasy, Vayne is number one.",
	"TEAMFIGHT" : "After getting 2 attack speed items, typically Blade of the Ruined King and Phantom Dancer, a good Vayne player will look to fight because she can do what she does best: melt enemies. Her W: Silver Bolts is arguably the highest scaling damage ability in League, and good positioning on her E: Condemn typically means a dead enemy. ",
	"DUELING" : "By level 13 and having her core attack speed items, Vayne can, in theory, 1v1 any champion, even some that are ahead in gold and levels. Her R: Final Hour is a powerful attack steroid that only gets better with max ranks in Q: Tumble as the invisibility can throw off enemies without oracles. A well-placed E: Condemn followed by a few Q: Tumbles and auto-attacks can clean up squishies and tanks alike thanks to max percentage health true damage.",
	"MECHANICS" : "Vayne is one of the most mechanically intensive marksmen in all of League. She only has one damaging abilities outside of her auto-attack, and even that does not extend past her auto-attack range. Therefore, the player must be extremely precise in positioning because one inch too close to the enemy could mean a locked down and dead Vayne.",
	}

Champ_List = [ASHE, CAITLYN, CORKI, DRAVEN, EZREAL,
    JHIN, JINX, KALISTA, KOG_MAW,LUCIAN, MFORTUNE,
    SIVIR, TRISTANA, TWITCH, VARUS, VAYNE]

print "Answer these 10 questions and see which ADC fits your playstyle the best!"
print""
trigger = raw_input("Press Enter to continue.")
print""
print "Enter Number Corresponding to your preffered Option"
print""
Player_Laning = int(raw_input("1. Rate how aggressive you are during laning phase:\n1 : Bro, just let me farm\n2 : Somewhat passive\n3 : Somewhat aggressive\n4 : Kill lane, YOLO\n"))
if Player_Laning == 1:
	Player_Laning = 0
elif Player_Laning == 2:
	Player_Laning = 33
elif Player_Laning == 3:
	Player_Laning = 67
elif Player_Laning == 4:
	Player_Laning = 100
print""
Player_Kiting = int(raw_input("2. Rate how good you are at kiting melee enemies:\n1 : How do I right click?\n2 : Mechanically shoddy\n3 : Average\n4 : Mechanically capable\n5 : Kassadin can't touch me\n"))
Player_Kiting = (int(Player_Kiting)-1)*25
print""
Player_Supp1 = int(raw_input("3. Which support would you rather lane with?\n1 : Blitzcranck\n2 : Soraka\n3 : Zyra\n"))
print""
Player_Dodging = int(raw_input("4. Rate your ability to predict or dodge enemy skillshots:\n1 : How did that even hit me?\n2 : Occassionally dodges\n3 : Often dodges\n4 : Jukes and mechanics all day\n"))
if Player_Dodging == 1:
	Player_Dodging = 0
elif Player_Dodging == 2:
	Player_Dodging = 33
elif Player_Dodging == 3:
	Player_Dodging = 67
elif Player_Dodging == 4:
	Player_Dodging = 100
print""
Player_Teamfighting = int(raw_input("5. Rate how comfortable you are in late game teamfights:\n1 : Way too stressful\n2 : Rather disengage\n3 : Either is fine\n4 : Rather fight\n5 : Time to carry, boys\n"))
Player_Teamfighting = (int(Player_Teamfighting)-1)*25
print""
Player_Supp2 = int(raw_input("6. Which support would you rather lane with?\n1 : Sona\n2 : Leona\n3 : Lux\n"))
print""
Player_Positioning = int(raw_input("7. Rate how often your deaths are a result of poor positioning or getting caught out\n1 : I'm always where I should be\n2 : Rarely happens\n3 : Sometimes\n4 : Happens often\n5 : PTSD from Blitzcrank\n"))
Player_Positioning = (int(Player_Positioning)-1)*25
print""
Player_Dueling = int(raw_input("8. Rate how comfortable you are in duels\n1 : Where did my support go?\n2 : Rarely engage\n3 : Often engage\n4 : See champion, kill champion\n"))
if Player_Dueling == 1:
	Player_Dueling = 0
elif Player_Dueling == 2:
	Player_Dueling = 33
elif Player_Dueling == 3:
	Player_Dueling = 67
elif Player_Dueling == 4:
	Player_Dueling = 100
print""
Player_Landing = int(raw_input("9. Rate your ability to land skillshots\n1 : Button mash\n2 : Occassionally lands\n3 : Often lands\n4 : Call me scripted\n"))
if Player_Landing == 1:
	Player_Landing = 0
elif Player_Landing == 2:
	Player_Landing = 33
elif Player_Landing == 3:
	Player_Landing = 67
elif Player_Landing == 4:
	Player_Landing = 100
print""
Player_Supp3 = int(raw_input("10. Which support would you rather lane with?\n1 : Morgana\n2 : Taric \n3 : Nautilus\n"))
print""
Player_Rank = int(raw_input("Finally, Tell you League\n1 : Bronze/Silver\n2 : Gold/Platinum\n3 : Diamond+\n"))
print""


for champs in Champ_List:
	champs["Player_avg"] = \
	((100 - abs(Player_Laning - champs["Laning"])) + \
	(100 - abs(Player_Kiting - champs["Kiting"])) + \
	((support(Player_Supp1, champs["Support1"]))*0.5) + \
	(100 - abs(Player_Dodging - champs["Dodgeing"])) + \
	(100 - abs(Player_Teamfighting - champs["TeamFighting"])) + \
	((support(Player_Supp2, champs["Support2"]))*0.5) + \
	(100 - abs(Player_Positioning - champs["Positioning"])) + \
	(100 - abs(Player_Dueling - champs["Dueling"])) + \
	(100 - abs(Player_Landing - champs["Landing"])) + \
	((support(Player_Supp3, champs["Support3"]))*0.5))/8.5

	champs["Player_avg"] = format(champs["Player_avg"], ".0f")
print ASHE["Player_avg"]
print ""
print "Your Scores:"
print ""
m = 101
while m > 0:
	for champs in Champ_List:
		if str(champs["Player_avg"]) == str(m):
			print champs["Name"], " "*(12-len(champs["Name"])) ,champs["Player_avg"]
	m -= 1 
print ""
champ_detail = raw_input("Enter champ name you would like information about:\n")


def champ_details(n):
	for champs in Champ_List:
		if champs["Name"].lower() == n.lower():
			print"**********"
			print ""
			print champs["Name"], ":",champs["Tag"]
			print ""
			print "Laning: " + champs["LANING"]
			print ""
			print "Teamfighting: " +  champs["TEAMFIGHT"]
			print ""
			print "Dueling: " + champs["DUELING"]
			print ""
			print "Mechanics: " + champs["MECHANICS"]
			print ""
	trigger2 = raw_input("Would you like to see another champs detials? (Enter \"y\" or \"n\")\n")
	print""
	if trigger2 == "y":
		champ_detail = raw_input("Enter champ name you would like information about:\n")
		return champ_details(champ_detail)
champ_details(champ_detail)