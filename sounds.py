'''
Module name: sounds
Date created: 27.12.2020

Contains list of phonemes in Bengali. Sound groups:
vowels/consonants
phonation type-- voiced, voiceless, aspirated
PoA-- labial, denti-alveolar, retroflex, post-alveolar, velar
MoA-- stop, nasal, fricative, semivowel
'''


def list(x):
    ''' x = input string; output: list of elements in string (separator = " ")'''
    l = x.split(" ")
    return l

#group names
gs = "vowel consonant voiced voiceless aspirated nasal fricative stop semivowel labial dentialveolar retroflex postalveolar velar"
groups = list(gs)


#vowels
vs = "i ^i ~i ee ^ee E ^E A ^A a oh ^oh u ^u oi ou ^ou aa ^aa"
vowel = list(vs)

#consonants
cs = "k kh g gh ch chh j jh ^n Y sh T Th D Dh rr R tt tth dd ddh n l s p ph b bh m h"
consonant = list(cs)

#all phonemes
ps = cs+" "+vs
phonemes = list(ps)


## Sound groups

#voiced
vois = vs+" g gh j jh ^n Y D Dh n rr R dd ddh l b bh m"
voiced = list(vois)

#voiceless
vls = "k kh ch chh sh T Th tt tth s p ph h"
voiceless = list(vls)

#aspirated
asps = "kh gh chh jh Th Dh tth ddh ph bh"
aspirated = list(asps)


# MoA (manner of articulation) grouping

#nasals
ns = "^i ^ee ^E ^A ^oh ^u ^ou ^aa ^n n m"
nasal = list(ns)

#fricatives
fs = "s sh h"
fricative = list(fs)

#stops
ss = "k kh g gh T Th D Dh tt tth dd ddh p ph b bh"
stop = list(ss)

#semi-vowels
svs = "Y r l"
semivowel = list(svs)


# PoA (place of articulation) grouping

#labial
ls = "p ph b bh m"
labial = list(ls)

#denti-alveolar
ds = "tt tth dd ddh n l s"
dentialveolar = list(ds)

#retroflex
rs = "T Th D Dh"
retroflex = list(rs)

#postalveolar
pas = "ch chh j jh Y sh T Th D Dh"
postalveolar = list(pas)

#velar
ves = "k kh g gh ^n"
velar = list(ves)



