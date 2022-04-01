from snake_body import Snake, Block

def test_block_str():
    b1 = Block(0)
    b1.make_block(20, 0)
    # print(b1)

    b2 = Block(1)
    b2.make_block(40, 0)

    l1 = []
    l1.append(b1)
    l1.append(b2)

    str_blocks = ""
    for b in l1:
        str_blocks += str(b) + ", "

    print(str_blocks)



def test_snake_str():
    s1 = Snake()
    s1.snake_parts = [[160, 0], [160, 20], [180, 20], [200, 20], [200, 0], [180, 0], [160, 0], [140, 0]]
    print(s1.snake_parts)
