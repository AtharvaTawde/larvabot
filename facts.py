import random

general = [
    "Most American car horns honk in the key of F.",
    "Every time you lick a stamp, you consume 1/10 of a calorie.",
    "The average person falls asleep in seven minutes.",
    "Studies show that if a cat falls off the seventh floor of a building it has about thirty percent less chance of surviving than a cat that falls off the twentieth floor. It supposedly takes about eight floors for the cat to realize what is occurring, relax and correct itself.",
    "Your stomach has to produce a new layer of mucus every 2 weeks otherwise it will digest itself.",
    "The citrus soda 7-UP was created in 1929; '7' was selected after the original 7-ounce containers and 'UP' for the direction of the bubbles.",
    "101 Dalmatians, Peter Pan, Lady and the Tramp, and Mulan are the only Disney cartoons where both parents are present and don't die throughout the movie.",
    "'Stewardesses' is the longest word that is typed with only the left hand.",
    "To escape the grip of a crocodile's jaws, push your thumbs into its eyeballs - it will let you go instantly.",
    "Reindeer like to eat bananas.",
    "No word in the English language rhymes with month, orange, silver and purple.",
    "The electric chair was invented by a dentist.",
    "More people are killed annually by donkeys than airplane crashes.",
    "A 'jiffy' is a unit of time for 1/100th of a second.",
    "Because of the rotation of the earth, an object can be thrown farther if it is thrown west.",
    "The average person spends 6 months of their life sitting at red lights.",
    "In 1912 a law passed in Nebraska where drivers in the country at night were required to stop every 150 yards, send up a skyrocket, wait eight minutes for the road to clear before proceeding cautiously, all the while blowing their horn and shooting off flares.",
    "More Monopoly money is printed in a year, than real money throughout the world.",
    "Caesar salad has nothing to do with any of the Caesars. It was first concocted in a bar in Tijuana, Mexico, in the 1920's.",
    "One quarter of the bones in your body are in your feet.",
    "Crocodiles and alligators are surprisingly fast on land.  Although they are rapid, they are not agile.  So, if being chased by one, run in a zigzag line to lose them.",
    "Seattle’s Fremont Bridge rises up and down more than any drawbridge in the world.",
    "Right-handed people live, on average; nine years longer than left handed people.",
    "Ten percent of the Russian government's income comes from the sale of vodka.",
    "In the United States, a pound of potato chips costs two hundred times more than a pound of potatoes.",
    "A giraffe can go without water longer than a camel.",
    "A person cannot taste food unless it is mixed with saliva. For example, if a strong-tasting substance like salt is placed on a dry tongue, the taste buds will not be able to taste it. As soon as a drop of saliva is added and the salt is dissolved, however, a definite taste sensation results. This is true for all foods.",
    "Nearly 80% of all animals on earth have six legs.",
    "Ninety percent of all species that have become extinct have been birds.",
    "There is approximately one chicken for every human being in the world.",
    "Each of us generates about 3.5 pounds of rubbish a day, most of it paper.",
    "A rainbow can be seen only in the morning or late afternoon. It can occur only when the sun is 40 degrees or less above the horizon.",
    "It has NEVER rained in Calama, a town in the Atacama Desert of Chile.",
    "It costs more to buy a new car today in the United States than it cost Christopher Columbus to equip and undertake three voyages to and from the New World.",
    "The plastic things on the end of shoelaces are called aglets.",
    "Daylight Saving Time is not observed in most of the state of Arizona and parts of Indiana.",
    "Ants closely resemble human manners:  When they wake, they stretch & appear to yawn in a human manner before taking up the tasks of the day.",
    "Bees have 5 eyes. There are 3 small eyes on the top of a bee's head and 2 larger ones in front.",
    "Count the number of cricket chirps in a 15-second period, add 37 to the total, and your result will be very close to the actual outdoor Fahrenheit temperature.",
    "One-fourth of the world's population lives on less than $200 a year.  Ninety million people survive on less than $75 a year.",
    "Butterflies taste with their hind feet.",
    "If one places a tiny amount of liquor on a scorpion, it will instantly go mad and sting itself to death.",
    "It is illegal to hunt camels in the state of Arizona.",
    "In eighteenth-century English gambling dens, there was an employee whose only job was to swallow the dice if there was a police raid.",
    "There are no clocks in Las Vegas gambling casinos.",
    "The human tongue tastes bitter things with the taste buds toward the back. Salty and pungent flavors are tasted in the middle of the tongue, sweet flavors at the tip!",
    "The first product to have a bar code was Wrigley’s gum.",
    "When you sneeze, air and particles travel through the nostrils at speeds over 100 mph. During this time, all bodily functions stop, including your heart, contributing to the impossibility of keeping one's eyes open during a sneeze.",
    "Celery has negative calories! It takes more calories to eat a piece of celery than the celery has in it.",
    "The average lead pencil will draw a line 35 miles long or write approximately 50,000 English words.  More than 2 billion pencils are manufactured each year in the United States. If these were laid end to end they would circle the world nine times.",
    "The pop you hear when you crack your knuckles is actually a bubble of gas burning.",
    "A literal translation of a standard traffic sign in China: 'Give large space to the festive dog that makes sport in the roadway.'",
    "You burn more calories sleeping than you do watching TV.",
    "In a lifetime the average human produces enough quarts of spit to fill 2 swimming pools.",
    "It's against the law to doze off under a hair dryer in Florida",
    "It's against the law to slap an old friend on the back in Georgia",
    "It's against the law to Play hopscotch on a Sunday in Missouri.",
    "The human heart creates enough pressure to squirt blood 30ft.",
    "It has been estimated that humans use only 10% of their brain.",
    "Most Egyptians died by the time they were 30 about 300 years ago,",
    "1 in every 4 Americans has appeared someway or another on television.",
    "1 in 8 Americans has worked at a McDonalds restaurant.",
    "70% of all boats sold are used for fishing.",
    "Studies have shown that children laugh an average of 300 times/day and adults 17 times/day, making the average child more optimistic, curious, and creative than the adult.",
    "You were born with 300 bones, but by the time you are an adult you will only have 206.",
    "If you go blind in one eye you only lose about one fifth of your vision but all your sense of depth.",
    "The strongest muscle (Relative to size) in the body is the tongue."
]

history = [
    "The very first bomb dropped by the Allies on Berlin during World War II Killed the only elephant in the Berlin Zoo.",
    "The shortest war in history was between Zanzibar and Englandin 1896. Zanzibar surrendered after 38 minutes.",
    "In ancient Egypt, servants were smeared with honey to attract flies away from the pharaoh.",
    "Roman Catholics in Bavaria founded a secret society in 1740 called the Order of the Pug. New members had to wear dog collars and scratch at the door to get in.",
    "Henry VIII of England had people who were called 'Grooms of Stool' whose job it was to wipe his bottom. During his reign, he had four such people, all of whom were knighted.",
    "Before Abraham Lincoln became a politician, he was a champion wrestler. With more than 300 bouts under his belt, Lincoln only lost one match in his career and was inducted into the National Wrestling Hall Of Fame in 1992.",
    "Until the early 20th century in Mongolia, criminals could be locked up in a wooden box as punishment, sometimes left to die of starvation.",
    "In 1923, jockey Frank Hayes won a race at Belmont Park in New York despite being dead. He suffered a heart attack mid-race, but his body stayed in the saddle until his horse crossed the line for a 20-1 outsider victory.",
    "All British tanks since 1945 have included equipment to make tea."
    "Hitler, Mussolini, and Stalin were all nominated for the Nobel Peace Prize.",
    "Roman Emperor Gaius, also known as Caligula, made one of his favorite horses a senator.",
    "The town of Salem, New Jersey once held a trial against tomatoes in 1820 because of the widespread belief they were poisonous. The case ended after Colonel Robert Gibbon Johnson ate a basket of tomatoes without ill consequence.",
    "In 1942, the U.S. Army fired 1,400 anti-aircraft rounds during what was thought to be a Japanese air raid over Los Angeles County. It turned out to be a false alarm. Five civilians died as an indirect result.",
    "In 1493, Columbus thought he saw mermaids -- they were 'not as pretty as they are depicted, for somehow in the face they look like men.' It's suspected he saw a manatee."
    "Chickens may have been first domesticated by humans for cockfighting, not for food.",
    "During the 1800s in the United States, it was considered a cruel and unusual punishment to feed lobster to prisoners and convicts."
]

math = [
    "You multiply Pi multiplied by the radius squared to find the area and multiply area by height to find the volume, That means the volume of a pizza that has a nominal radius of (z) and height (a) will, of course, be: Pi × z × z × a",
    "Strangely, if you enter Pi to two decimal places (3.14) in the your calculator and look at it in the mirror, you'll see it spells 'pie'.",
    "The spiral shapes of sunflowers and other patterns in nature follow a Fibonacci sequence, where adding the two preceding numbers in the sequence gives you the next (1, 1, 2, 3, 5, 8, etc.)",
    "It only takes 23 people to enter a room to give you an evens chance that two of them have the same birthday. With 75 people in the room the chances rise to 99 per cent.",
    "If you multiply 111,111,111 × 111,111,111 you get 12,345,678,987,654,321 - a palindrome number that reads the same forwards or backwards. And that works all the way back down to 11 x 11 (121) or just 1 x 1 (1).",
    "A googolplex is 10 to the power of a googol, or 10 to the power of 10 to the power of 100. Our known universe doesn't have enough space to actually write that out on paper. If you try to do that sum on a computer, you'll never get the answer, because it won't have enough memory.",
    "1 can actually equal 0.999. Proofs:\n\nProof 1:\nIf N = 0.999, then 10N = 9.99.\n10N - N is therefore 9.99 - 0.999 therefore 9N = 9 therefore N =1\n\nProof 2:\nIf N = 0.999 then N divided by 9 is 0.111\nExpress this as the equation:\n0.111 = 1/9\nMultiplying both sides by 9 produces:\n0.999 = 1",
    "2 and 5 are the only primes that end in 2 or 5.",
    "From 0 to 1,000, the letter \"A\" only appears in 1,000 (\"one thousand\").",
    "'FOUR' is the only number in the English language that is spelt with the same number of letters as the number itself.",
    "A circle has the largest area of any shape with the same perimeter.",
    "A circle has the shortest perimeter of any shape with the same area."
]

science = [
    "Babies have abound 100 more bones than adults.", 
    "The Eiffel Tower can be 15 cm taller during the summer.",
    "20% of Earth’s oxygen is produced by the Amazon rainforest.",
    "Some metals are so reactive that they explode on contact with water.",
    "A teaspoonful of neutron star would weigh 6 billion tons.",
    "Hawaii moves 7.5cm closer to Alaska every year.",
    "Chalk is made from trillions of microscopic plankton fossils.",
    "In 2.3 billion years it will be too hot for life to exist on Earth.",
    "Polar bears are nearly undetectable by infrared cameras.",
    "It takes 8 minutes, 19 seconds for light to travel from the Sun to the Earth.",
    "If you took out all the empty space in our atoms, the human race could fit in the volume of a sugar cube.",
    "Stomach acid is strong enough to dissolve stainless steel.",
    "The Earth is a giant magnet.",
    "Venus is the only planet to spin clockwise.",
    "A flea can accelerate faster than any Space Shuttle."
    "Camels don't actually store water in their humps."
    "Salamanders can extend their tongues a long way.",
    "Space is completely silent.",
    "Neutron stars can spin 600 times per second."
]


def output(message):
    response = "Enter in a valid argument. Examples: !fact history, !fact math, !fact general, !fact science, etc."
    if message.content == "!fact":
        return (f"```{response}```")
    elif "!fact " in message.content:
        fact_type = message.content.split(' ')[1].lower()
        if fact_type == "general":
            response = random.choice(general)
        elif fact_type == "history":
            response = random.choice(history)
        elif fact_type == "math":
            response = random.choice(math)
        elif fact_type == "science":
            response = random.choice(science)
        return (f"```{response}```")
    else:
        return "```Maybe you're trying to type !fact?```"
