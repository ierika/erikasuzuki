import random


class Chuck:
    facts = [
        "Chuck Norris can kill two stones with one bird.",
        "When Chuck Norris is doing a push-up, he is not lifting himself up but pushing the earth down.",
        "Chuck Norris is the reason Waldo is hiding.",
        "When Chuck Norris was born he drove his mom home from the hospital.",
        "Chuck Norris has a diary. It's called the Guinness Book of World Records.",
        "Chuck Norris can divide by 0.",
        "Chuck Norris can hear sign language.",
        "Chuck Norris tells Simon what to do.",
        "Chuck Norris's Blood Type is AK-47.",
        "Chuck Norris' dog is trained to pick up his own poop because Chuck Norris will not take shit from anyone.",
        "Chuck Norris can speak braille.",
        "Chuck Norris can unscramble an egg.",
        "Sharks have a Chuck Norris week",
        "Chuck Norris can understand women.",
        "Chuck Norris counted to infinity – Twice.",
        "Death once had a near-Chuck experience.",
        "Chuck Norris doesn't dial the wrong number. You answered the wrong phone.",
        "Chuck Norris knows Victoria's secret.",
        "If Chuck Norris was a Spartan in the movie 300, the movie would be called 1.",
        "When Chuck Norris turned 18, his parents moved out.",
        "When Chuck Norris swims in the ocean, the sharks are in a steel cage.",
        "Chuck Norris will never have a heart attack. His heart isn't nearly foolish enough to attack him.",
        "Chuck Norris once kicked a horse in the chin. Its descendants today are known as giraffes.",
        "Chuck Norris doesn't breathe air. He holds air hostage.",
        "Chuck Norris can delete the Recycle Bin.",
        "Chuck Norris has already been to Mars. That's why there are no signs of life.",
        "Chuck Norris wears sunglasses so that his eyes won't hurt the sun.",
        "Chuck Norris was born May,6 1945. Nazi Germany surrendered May,7 1945. \
         Coincidence? I think not."
    ]

    def get_random_fact(self):
        random.shuffle(self.facts)
        return self.facts[0]
