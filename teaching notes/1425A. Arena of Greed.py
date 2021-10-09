# C++解决的

# # include <bits/stdc++.h>
# using
# namespace
# std;
# typedef
# long
# long
# ll;
# const
# int
# maxn = 4e5 + 7;
# const
# int
# mod = 1e9 + 7;
# char
# x;
# ll
# n, t, s;
# int
# main()
# {
#     cin >> t;
# while (t - -)
#     {
#         cin >> n;
#     s = 0;
#     int
#     k = 0;
#     while (n)
#         {
#         if (k % 2 == 0)
#         {
#         if (n % 2 == 1)
#         {
#             s + +;
#         n - -;
#         }
#         else
#         {
#         if ((n / 2) % 2 == 0 & & n > 4)
#         {
#             s + +;
#         n - -;
#         }
#         else
#         {
#             s += n / 2;
#         n /= 2;
#         }
#         }
#         }
#         else
#         {
#         if (n % 2 == 1)
#         n - -;
#         else if ((n / 2) % 2 == 0 & & n > 4)
#         {
#         n--;
#         }
#         else
#         n /= 2;
#
#         }
#         k++;
#         }
#         cout << s << endl;
#     }
#     return 0;
# }
