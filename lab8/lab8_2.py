def main():
    line = "the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car"
    # your code goes here
    tuple_words=tuple(sorted(line.split(" "), reverse=True))
    counts=dict()

    how_many_difference_words=0
    for i in range(len(tuple_words)):
        #counts[tuple_words[i]]=counts.get(tuple_words[i],0)+1
        if tuple_words[i] not in counts:
            counts[tuple_words[i]]=1
            how_many_difference_words+=1
        else:
            counts[tuple_words[i]]=counts[tuple_words[i]]+1
        
    print("There are",len(tuple_words),"words with",how_many_difference_words,"in difference")
    for name, number in sorted (counts.items(), key=lambda item:item[1], reverse=True):
        print('Word: "'+str(name)+'" --- Counts:'+str(number))


# You are not allowed to modify the following codes
if __name__ == "__main__":
    main()
