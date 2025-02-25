import argparse
from .color import Color as C

def get_options():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--jornal", "-j", type=str, required=False,
                        default="NEXO",
                        help="Qual jornal acessar: G1, NEXO, JAV",
                        metavar="STR")
    
    parser.add_argument("--canal", "-c", type=str, required=False,
                        default=None,
                        help="Canal de RSS do jornal escolhido [apenas G1]",
                        metavar="STR")

    parser.add_argument("--data", '-d', type=int, required=False,
                        default=-1,
                        help="Pegar apenas matérias lançadas desde N dias atrás",
                        metavar="N")
    
    parser.add_argument("--search", "-s", type=str, required=False,
                        default=None,
                        help="Busca por matérias com as palavras dadas",
                        metavar="STR",
                        nargs='+')
    
    parser.add_argument("--hue", "-u", type=str, required=False,
                        default="blue",
                        help="Cor usada para o nome do jornal: {0}, {1}, {2}".format(
                            C.red("RED"), C.green("GREEN"), C.blue("BLUE")),
                        metavar="STR")

    parser.add_argument("--installpath", type=str, required=False,
                        default=".",
                        help="Caminho para a instalação do `cli-news`",
                        metavar="PATH")

    return parser.parse_args()
