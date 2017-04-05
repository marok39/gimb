import sys
import os
import filecmp as fcmp
import re
import multiprocessing as mp


def shell(c, testfolder, i):
    if "nt" not in os.name:
        os.system("python3 " + c + ".py < " \
            + testfolder + "/input-" + str(i) + ".txt >" \
            + testfolder + "/output-" + str(i) + ".txt")
    else:
        os.system("py -3 " + c + ".py < " \
            + testfolder + "/input-" + str(i) + ".txt >" \
            + testfolder + "/output-" + str(i) + ".txt")


def test(c):
    n = re.findall('\d+', c)[0]
    testfolder = "test-" + n
    filelist = os.listdir(testfolder)
    num_of_tests = sum(1 if f.startswith("input") else 0 for f in filelist)
    correct = 0
    timeout = False

    print("Testiram " + testfolder + "...")

    for i in range(1, num_of_tests + 1):
        p = mp.Process(target=shell, args=(c,testfolder,i,))
        p.start()
        p.join(5)

        if p.is_alive():
            p.terminate()
            p.join()
            timeout = True

        f1 = testfolder + "/output-" + str(i) + ".txt"
        f2 = testfolder + "/result-" + str(i) + ".txt"
        if fcmp.cmp(f1, f2):
            print(str(i) + ". primer: " + hilite("Pravilno!", True))
            correct += 1
        elif timeout:
            print(str(i) + ". primer: " + hilite("Timeout", False))
        else:
            print(str(i) + ". primer: " + hilite("Nepravilno...", False))

        timeout = False

    if correct == num_of_tests:
        print(hilite("Cestitke. Vse pravilno!", True))
    else:
        print("Rezultat: " + str(correct) + "/" + str(num_of_tests) + ".")


def hilite(string, status):
    if "nt" not in os.name:
        attr = ['32'] if status else ['31']
        return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
    return string


def main():
    if len(sys.argv) == 2:
        c = sys.argv[1]
        test(c)
    else:
        print("Podaj ime naloge kot 'naloga1' (brez .py)...")

if __name__ == "__main__":
    main()
