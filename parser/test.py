import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from SmallCLexer import SmallCLexer
from SmallCParser import SmallCParser
from SmallCListener import SmallCListener
from generator import GeneratorVisitor

if __name__ == '__main__':
    inputFile = FileStream(sys.argv[1])
    lexer = SmallCLexer(inputFile)
    stream = CommonTokenStream(lexer)
    parser = SmallCParser(stream)
    tree = parser.smallc_program()
    print(Trees.toStringTree(tree, None, parser))
    # listener = SmallCListener()
    # walker = ParseTreeWalker()
    # walker.walk(listener, tree)

    output_file = None # open(sys.argv[2], "w+")
    eval = GeneratorVisitor(output_file)
    eval.visit(tree)
    eval.print()
    # output_file.close()
