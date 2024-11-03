import math
import time

def paragraph(ch):
    word=["Crickets","chirp","Rusted", "keyhole","Tangy","lemonade","Sun","dappled","path","Worn","leather","jacket","Whispering","wind","Flour","dusted","apron","Flour","dusted","apron","Twinkling stars","Dusty attic","Melodious laughter","Faded photograph","Moss-covered stone","Rumbling thunder","Fragile butterfly","Creaking swing set","Overflowing bookshelf","Spicy chili peppers","Pattering raindrops","Roaring campfire","Ancient ruins","Sparkling ocean waves","Glowing fireflies","Hidden treasure map","Juicy watermelon","Howling wind","Crinkled parchment scroll","Secret garden","Soothing rain","Glowing embers","Echoing footsteps","Sun-kissed skin","Fizzy soda pop","Whispering secrets","Glistening tears","Heavy heart","Fragile hope","Soaring eagle","Hidden message","Tangled yarn ball","Whispering leaves","Dusty attic","Fragile trust","Creaking floorboards","Rumbling train","Sun-drenched meadow","Salty sea breeze","Soothing melody","Endless possibilities","Faded memories"]
    para=["The aroma of freshly brewed coffee filled the air, swirling around the enticing scent of cinnamon rolls baking in the oven. Sunlight streamed through the kitchen window, casting a warm glow on the mismatched mugs lining the table. A gentle breeze ruffled the curtains, carrying the sweet melody of birds chirping outside. It was a perfect morning, filled with the promise of a relaxing day","The bustling marketplace was a kaleidoscope of sights, sounds, and smells. Vendors hawked their wares in colorful stalls, their voices a cacophony that somehow managed to blend into a rhythmic chant. The air hung heavy with the aroma of spices, grilled meats, and exotic fruits. Crowds weaved through the narrow aisles, their laughter and chatter adding to the vibrant atmosphere. It was a sensory overload in the best way possible","The weight of the backpack felt heavy on her shoulders, but she pressed on, her determination fueled by the breathtaking view that awaited her at the summit. The mountain trail wound its way through a dense forest, dappled sunlight filtering through the leaves and casting a cool shade on the path. The crisp mountain air filled her lungs with each labored breath, and the distant sound of a cascading waterfall added to the tranquility of the hike","The once grand library had fallen into disrepair. Cobwebs draped the dusty shelves, and peeling wallpaper hung from the damp walls. The silence was broken only by the occasional creak of the floorboards or the rustle of a stray page turning in a forgotten book. Yet, amidst the decay, there was a sense of history, a whisper of the countless stories that had once filled these halls","The museum was a labyrinth of ancient artifacts, each one a portal to a bygone era. A towering statue of a pharaoh guarded the entrance to the Egyptian exhibit, while intricate tapestries adorned the walls of the medieval hall. In the natural history section, a life-sized dinosaur skeleton loomed overhead, its sharp teeth and massive claws a reminder of the prehistoric world. It was a journey through time, a chance to marvel at the ingenuity and creativity of humankind throughout history","The concert hall buzzed with anticipation as the audience waited for the performance to begin. The air crackled with nervous energy, punctuated by excited whispers and rustling programs. The grand orchestra took their places on stage, their instruments gleaming under the spotlight. A hush fell over the crowd as the conductor raised their baton, and the first notes of the symphony filled the air. It was a moment of pure magic, where music transported everyone to a world of emotions","The bustling city streets were a constant stream of activity. Taxis honked their horns, pedestrians hurried along the sidewalks, and vendors hawked their wares from overflowing carts. Skyscrapers scraped the clouds, their glass windows reflecting the vibrant city lights. The energy was infectious, a constant hum that vibrated through the concrete jungle. It was a place where dreams were chased, fortunes were made, and stories unfolded on every corner","The cozy bookstore was a haven for bibliophiles. Floor-to-ceiling shelves overflowed with books of every genre imaginable, their spines a rainbow of colors. The air hung heavy with the comforting scent of old paper and leather. An armchair sat tucked away in a quiet corner, beckoning readers to curl up with a good book. It was a world of imagination, where adventures unfolded on every page and characters came alive in the reader's mind","The tropical rainforest was a riot of color and sound. Towering trees formed a dense canopy overhead, their leaves filtering the sunlight into a dappled pattern on the forest floor. Exotic birds squawked and chirped in the branches, their vibrant plumage a marvel to behold. Strange insects buzzed amongst the lush vegetation, and the air thrummed with the constant hum of life. It was a world teeming with diversity, a testament to the power of nature","The starry night sky was a breathtaking spectacle. Countless stars twinkled like diamonds scattered across a vast canvas of black velvet. The Milky Way stretched across the heavens, a luminous band of light formed by billions of distant suns. The moon cast a silvery glow on the landscape, bathing everything in an ethereal light. It was a humbling sight, a reminder of our place in the vast universe"]
    sent=["The determined butterfly flapped its wings, determined to reach the other side of the meadow","Raindrops pattered a whimsical rhythm against the old library window","A stray strand of spaghetti clung stubbornly to the chef's hat","The aroma of freshly baked cookies filled the kitchen with a warm welcome","The astronaut gazed out the window, mesmerized by the swirling blue marble of Earth","The rickety swing set creaked in the gentle breeze, whispering secrets of childhood summers","The flickering candlelight cast dancing shadows on the cobblestone street","The worn leather armchair held a thousand stories within its folds","With a mischievous grin, the child hid behind the oversized curtains","With a mischievous grin, the child hid behind the oversized curtains","The rusty compass needle spun erratically, refusing to point north","The rhythmic clacking of the typewriter filled the room with a sense of urgency","The ancient library held the weight of countless forgotten memories","The mischievous glint in the cat's eyes promised trouble","The weightless sensation of floating in the pool made her feel like a mermaid","The chirping crickets serenaded the starlit night sky","The aroma of freshly cut grass signaled the approach of summer","The old rocking chair creaked a lullaby as the baby drifted off to sleep","The sound of crashing waves echoed against the rocky cliffs","The dusty attic held treasures waiting to be rediscovered","The morning fog created an ethereal atmosphere in the city park."]
    import random
    if len(ch)==0:
            return "Excuse me you not leave it empty like this"
            ch=0
    elif ch.isdigit():
        return "Your have enterd the wrong choise damit"
        ch=0
    elif " " in ch:
        ch=ch.strip()
    if (ch!=0):
        ch=ch.title()
        if (ch=="Word")or(ch=="Words")or(ch=="w")or(ch=="W"):
            return random.choice(word)
        elif(ch=="Sentence")or (ch=="Sentences")or(ch=="sent")or(ch=="Para")or(ch=="s")or(ch=="S"):
            return random.choice(sent)
        elif(ch=="Paragraph")or (ch=="Paragraphs")or(ch=="para")or(ch=="Para")or(ch=="p")or(ch=="P"):
            return random.choice(para)
        else:
            return "You have enterd the wrong choise"


def check(origin_string,type):
  global mist
  mist=""
  while True:
      if (origin_string!=type):
          print("type agin")
          type=input("==>")
          mist=mist+type+" "
      else:
          break
  mist=mist.split(" ")
  mist=len(mist)-1
  if (mist==0):
    mist=0

print("Welcome to my typing test \n You can choose option: \n * Word \n * Sentence \n * Paragraph")
tword=0
type2=""
type=""
ch=input("Enter the your option here:")
input("Press enter the Start")
epoch=time.time()
while True:
  if (ch[0]=="w"or ch[0]=="W"):
    for i in range(1,11):
      w=paragraph("word")
      print("*",w)
      #time.sleep(2)# to automate the tester
      type=input("==>")
      check(w,type)
      type2=type2+type+" "
    type2=type2.split(" ")
    break
  elif(ch[0]=="s"or  ch[0]=="S"):
    for i in range(1,6):
      s=paragraph("sentence")
      print("*",s)
      #time.sleep(2)
      type=input("==>")
      check(s,type)
      type2=type2+type+" "
    type2=type2.split(" ")
    break
  elif(ch[0]=="p"or ch[0]=="P"):
    p=paragraph("paragraph")
    print("*",p)
    #time.sleep(5)
    type=input("==>")
    check(p,type)
    type2=type2+type+" "
    type2=type2.split(" ")
    break
min=math.ceil(time.time()-epoch)/60
tword=(len(type2)-1)+mist
accuracy=((len(type2)-1)/tword)*100
print("[Result] \n* WPM:",math.ceil((len(type2)-1)/min),"\n* Accuracy:",accuracy,"%")