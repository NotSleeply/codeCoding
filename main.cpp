#include <bits/stdc++.h>
using namespace std;

/**
 * 如何从 Order: KT202605070001, IMEI: 356789123456789, price: IDR 2,350,000
 * 解析出其中的合法的
 * order no， imei， price，其中price转换成2350000
 */
string s;

int main(void)
{
    if (!getline(cin, s))
    {
        return 0;
    }

    regex pattern(R"(Order:\s*([A-Za-z0-9]+),\s*IMEI:\s*(\d+),\s*price:\s*IDR\s*([0-9,]+))");
    smatch match;
    if (!regex_search(s, match, pattern))
    {
        return 0;
    }
    
    string orderNo = match[1].str();
    string imei = match[2].str();
    string priceRaw = match[3].str();

    string price;
    for (char c : priceRaw)
    {
        if (isdigit(static_cast<unsigned char>(c)))
        {
            price.push_back(c);
        }
    }

    cout << orderNo << "\n"
         << imei << "\n"
         << price << "\n";
    return 0;
}
