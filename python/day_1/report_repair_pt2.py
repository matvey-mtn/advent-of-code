def find_3_entries_with_sum(input_list, requested_sum):
    report = sorted(input_list)

    fixed_pointer = 0
    head_pointer = fixed_pointer + 1
    tail_pointer = len(report) - 1

    # result = []
    # outer loop increments fixed_pointer
    while fixed_pointer + 1 < tail_pointer:
        # inner loop running on sub-list: report[head_pointer:tail_pointer]
        while head_pointer < tail_pointer:
            report_sum = report[fixed_pointer] + report[head_pointer] + report[tail_pointer]
            if report_sum > requested_sum:
                tail_pointer -= 1
            elif report_sum < requested_sum:
                head_pointer += 1
            else:
                print(report[fixed_pointer] * report[head_pointer] * report[tail_pointer])
                break

        fixed_pointer += 1
        # reset pointers
        head_pointer = fixed_pointer + 1
        tail_pointer = len(report) - 1


expense_report = [
    1735, 1700, 1358, 1908, 1634, 2006, 762, 1492, 1917, 1591, 1571, 1283, 1744, 1815, 1383, 1787,
    1832, 1032, 1845, 1406, 1978, 1263, 1450, 1364, 1594, 1877, 1346, 1695, 1501, 1266, 1729, 1476,
    1558, 1684, 1295, 1267, 1341, 1415, 1491, 1640, 1756, 1330, 1987, 1969, 1844, 1706, 1654, 1580,
    1405, 1419, 1367, 1277, 1992, 1953, 1499, 1470, 2000, 1739, 1889, 1670, 1776, 1798, 1308, 1890,
    1626, 1284, 1315, 1869, 1514, 1214, 1648, 1418, 1329, 1795, 1385, 1477, 1984, 1796, 1515, 2001,
    1155, 1800, 1965, 1971, 1100, 1650, 1686, 1911, 1560, 1912, 1721, 1658, 1738, 1885, 1028, 266,
    1989, 1704, 1388, 1498, 1769, 1453, 925, 1588, 1828, 1024, 1671, 1998, 1942, 1636, 1382, 993,
    1703, 1475, 1391, 1970, 1841, 1952, 1446, 1347, 1395, 1440, 1980, 1386, 1922, 1857, 1291, 1808,
    1335, 1876, 1576, 1436, 634, 1557, 1782, 1881, 1955, 1765, 1736, 1585, 1858, 1862, 989, 1661, 1757,
    1775, 1693, 1842, 1660, 1647, 870, 1928, 1597, 1420, 1646, 1821, 2009, 1866, 1947, 1593, 1788,
    1369, 1525, 1256, 1846, 1445, 1907, 1750, 1906, 1849, 765, 1342, 1811, 1260, 1466, 1424, 1823,
    1767, 1290, 1840, 1825, 1287, 1384, 1996, 1627, 1983, 1328, 1674, 1676, 1727, 1810, 1394, 799,
    1723, 1293, 1273, 1317, 1749, 1552, 1645
]

find_3_entries_with_sum(expense_report, 2020)
