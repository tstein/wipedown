
<pre>
     /               /
    /               /
   /               /
  /               /
 |       /       /
 |      |       |
 |      |       | ##### ####  #### ###    ###  #   # #   #
 \      |      /    #   #   # #    #  #  #   # #   # ##  #
  \    / \    /     #   ####  ###  #   # #   # # # # # # #
   \  /   \  /      #   #     #    #  #  #   # # # # #  ##
    \/     \/     ##### #     #### ###    ###   # #  #   #
</pre>


[Smudge attacks](http://static.usenix.org/event/woot10/tech/full_papers/Aviv.pdf), for the uninitiated, are a hilariously low-tech approach to
compromising lock screens on touchscreen devices. An attacker determines the
characters in a password or PIN from smudges left the last time the victim
unlocked his device, leaving the correct order of those characters as the only
thing standing between him and your data. With a 4-digit PIN, the bad guy must
try a maximum of 24 different codes. A password will require exponentially more
tries and save your bacon... unless your adversary has ever done an anagram.

Swiping keyboards (e.g., [Swype](http://www.swype.com/)) present another option: one large smudge that
covers its own tracks. *wipedown* is a password generator that produces
dictionary words with trails that will likely be extremely difficult to decode,
at least for adversaries of average intelligence and capability. It's a tool
for the casual tinfoil hat-wearer.

In the initial version, longer paths are always better and wipedown returns a
random string from above the 90th percentile. Rigorous try-it-and-see testing
has shown this to be a decent heuristic, but additional intelligence could
improve password quality further: for example, estimating how much a finger of a
given fatness will cover its own tracks.

