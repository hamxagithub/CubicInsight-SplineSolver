//#include <iostream>
//using namespace std;
//
//int fact(int n)
//{
//	int f = 1;
//	for (int i = 2; i <= n; i++)
//		f *= i;
//	return f;
//}
//
//void calculateBackwardDifferenceTable(float** y, int n)
//{
//	for (int i = 1; i < n; i++)
//	{
//		for (int j = n - 1; j >= i; j--)
//		{
//			y[j][i] = y[j][i - 1] - y[j - 1][i - 1];
//		}
//	}
//}
//
//float interpolate(float* x, float** y, int n, float v)
//{
//	float sum = y[n - 1][0];
//	float p = (v - x[n - 1]) / (x[1] - x[0]);
//	for (int i = 1; i < n; i++)
//	{
//		float prod = 1;
//		for (int j = 1; j <= i; j++)
//		{
//			prod *= (p+ j - 1) / j;
//		}
//		sum += prod * y[n - 1][i] / fact(i);
//	}
//	return sum;
//}
//
//int main()
//{
//	int n;
//	cout << "Enter the number of x or y coordinates : ";
//	cin >> n;
//	float* x = new float[n];
//	float** y = new float*[n];
//	for (int i = 0; i < n; ++i)
//	{
//		y[i] = new float[6];
//	}
//	cout << "Enter the X-Coordinates" << endl;
//	for (int i = 0; i < n; i++)
//	{
//		cout << "x" << i << " : ";
//		cin >> x[i];
//
//	}
//	cout << endl;
//	cout << "Enter the Y-Coordinates" << endl;
//	for (int i = 0; i < n; i++)
//	{
//		cout << "y" << i << " : ";
//		cin >> y[i][0];
//
//	}
//	cout << endl;
//	calculateBackwardDifferenceTable(y, n);
//
//	cout << "--------------******Backward Difference Table*******--------------------" << endl;
//	for (int i = 0; i < n; i++)
//	{
//		for (int j = 0; j <= i; j++)
//		{
//			cout << y[i][j] << "\t";
//		}
//		cout << endl;
//	}
//	cout << endl;
//	float v;
//	cout << "Enter the value of x for which y is to find : ";
//	cin >> v;
//	float sum = interpolate(x,y, n, v);
//
//	cout << "The Value of y at x : " << v << " is " << sum << endl;
//
//	for (int i = 0; i < n; ++i) 
//	{
//		delete[] y[i];
//	}
//	delete[] y;
//	delete[] x;
//}
