using System;
using System.Collections.Generic;

class Program
{
	static void buildTree(int root,
						  int parentOfRoot,
						  Dictionary<int, List<int>> edges)
		{
			List<int> node = edges[root];
			if (node.Contains(parentOfRoot)) node.Remove(parentOfRoot);

			foreach (int i in node) buildTree(i, root, edges);
		}


	static void DFS(int x, Dictionary<int, List<int>> edges,
					Dictionary<int, int> a,
					Dictionary<int, int> b,
					Dictionary<int, int> c)
		{
			foreach (int child in edges[x])
			{
				DFS(child, edges, a, b, c);
				a[x] = Math.Max(a[x], b[child] + 1 - c[child]);
				b[x] += c[child];
			}

			a[x] += b[x];
			c[x] = Math.Max(a[x], b[x]);
		}

	static int Main()
		{
			int nodesNumber = Int32.Parse(Console.ReadLine());

			if (nodesNumber == 1)
			{
				Console.Write(0);
				return 0;
			}

			var edges =	new Dictionary<int, List<int>>();
			for (int i = 0; i < nodesNumber + 1; i++)
			{
				edges[i] = new List<int>();
			}


			for (int i = 0; i < nodesNumber - 1; i++)
			{
				string[] pairStr = Console.ReadLine().Split(' ');
				int node1 = Int32.Parse(pairStr[0]);
				int node2 = Int32.Parse(pairStr[1]);

				edges[node1].Add(node2);
				edges[node2].Add(node1);
			}

			var <int, int> a = new Dictionary<int, int>();
			for (int i = 0; i < nodesNumber + 1; i++)
			{
				a[i] = 0;
			}
			var <int, int> b = new Dictionary<int, int>();
			for (int i = 0; i < nodesNumber + 1; i++)
			{
				b[i] = 0;
			}
			var <int, int> c = new Dictionary<int, int>();
			for (int i = 0; i < nodesNumber + 1; i++)
			{
				c[i] = 0;
			}

			int rootNode = 1;
			buildTree(rootNode, 0, edges);

			DFS(rootNode, edges, a, b, c);
			Console.WriteLine(c[rootNode]);

			return 0;
		}
}
