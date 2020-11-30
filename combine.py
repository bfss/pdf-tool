from PyPDF2 import PdfFileMerger
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--src1', required=True)
parser.add_argument('--src2', required=True)
parser.add_argument('--dst', required=True)
args = parser.parse_args()

merger = PdfFileMerger()

merger.append(open(args.src1, 'rb'))
merger.append(open(args.src2, 'rb'))

merger.write(args.dst)