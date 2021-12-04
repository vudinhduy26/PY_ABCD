import re
def count_smileys(arr):
    count = 0
    brr = [":)",";)",":D",";D",":-)",";-)",':-D',';-D',':~)',';~)',':~D',';~D']
    for i in arr:
        if i in brr:
            count += 1
    return count


def main():
    print(count_smileys([':)',':(',':D',':O',':;']))

if __name__ == "__main__":
    main()