using System;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Program
{
	static String readLine()
		{
			var sb =new StringBuilder();
			while (true)
			{
				char ch = Convert.ToChar(Console.Read());
				sb.Append(ch);
				if (ch == '\n') {
					break;
				}
			}
			return sb.ToString();
		}

	static int Main()
		{
			String[] kAndNStr = Console.ReadLine().Split(' ');
			Int32 n = Int32.Parse(kAndNStr[0]);
			Int32 k = Int32.Parse(kAndNStr[1]);

			String sourceLine = readLine().Trim();
			String[] numbersStr = sourceLine.Split(' ');
			var numbers = new List<Int64>();
			foreach (String numberStr in numbersStr)
			{
				numbers.Add(Int64.Parse(numberStr));
			}

			numbers.Sort();
			Int32 left_index = 0;
			Int32 right_index = n - 1;
			Int64 left_mul = 0;
			Int64 right_mul = 0;
			Int64 left_border = 0;
			Int64 right_border = 0;
			Int64 cur_mul = 1;
			Boolean isNegativeGreater = false;

			if (k % 2 != 0)
			{
				cur_mul = (cur_mul * numbers[right_index--]) %
					(1000000000 + 7);
				k--;
			}

			while (k != 0)
			{
				left_border = numbers[left_index] * numbers[left_index + 1];
				right_border = numbers[right_index] * numbers[right_index - 1];
				isNegativeGreater = left_border >= right_border;

				left_border %= (1000000000 + 7);
				right_border %= (1000000000 + 7);

				left_mul = (cur_mul * left_border) % (1000000000 + 7);
				right_mul = (cur_mul * right_border) % (1000000000 + 7);

				if (cur_mul < 0)
				{
					if (isNegativeGreater)
					{
						cur_mul = right_mul;
						right_index -= 2;
					}
					else
					{
						cur_mul = left_mul;
						left_index += 2;
					}
				}
				else
				{
					if (!isNegativeGreater)
					{
						cur_mul = right_mul;
						right_index -= 2;
					}
					else{
						cur_mul = left_mul;
						left_index += 2;
					}
				}

				k -= 2;
			}


			Console.WriteLine((cur_mul + 1000000000 + 7) % (1000000000 + 7));
			return 0;
		}
}
