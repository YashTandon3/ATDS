from atds2 import Vertex, Graph, Queue

def one_letter_off(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    return count == 1



def build_graph(word_file):
    with open(word_file, 'r', encoding = 'utf-8') as infile:
        words = [word.strip() for word in infile.readlines()]
    g = Graph()
    for word1 in words:
        for word2 in words:
            if one_letter_off(word1, word2):
                g.add_edge(word1, word2)
    return g



def traverse(g, start, finish):
    if finish != None:
        current = finish
        while current.get_previous() != None:
            print(current.get_key(), current.get_distance())
            current = current.get_previous()
        if current == start:
            print(current.get_key()) 
        else:
            print("Couldn't find a path!")
    else:
        print("Finishing vertex doesn't exist!")





def bfs(g, start):
    start.set_distance(0)
    start.set_previous(None)
    current = start
    q = Queue()
    print("Putting",current.get_key(),"on the queue")
    q.enqueue(current)
    while not q.is_empty():
        current = q.dequeue()
        print("Just pulled",current.__repr__(),"off the queue!")
        for neighbor in current.get_neighbors():
            if neighbor.get_color() == 'white':
                print("Processing",neighbor.get_key(),"by setting color to gray")
                neighbor.set_color('gray')
                neighbor.set_distance(current.get_distance() + 1)
                neighbor.set_previous(current)
                print("Adding",neighbor.__repr__(),"to the queue")
                q.enqueue(neighbor)
                print("Current queue:",q)
                input("[Enter] to continue...")
            elif neighbor.get_color() == 'gray':
                print("Found a gray neighbor",neighbor.get_key(),". It's already in the queue.")
            else:
                print("Found a black neighbor", neighbor.get_key(),"that's already been processed.")
        print("Finished processing",current.get_key())
        print("Setting it to black")
        current.set_color('black') 
        input("[Enter] to continue")







def main():
    g = build_graph('three-letter-words.txt')
    bfs(g, g.get_vertex('CAP'))
    for v in g:
        print(v)
    print(v.get_distance(), v.get_previous()) 
    traverse(g, g.get_vertex('CAP'), g.get_vertex('PAN'))

main()