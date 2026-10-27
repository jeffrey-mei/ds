#include <bits/stdc++.h>
using namespace std;
//背包问题  =>  DP   动态规划 
// n块宝石  m容量的背包 
//  4  8
//  w  v
//  2  5
//  3  6
//  4  7
//  5  8 
//状态  状态转移方程   无后效性  最优子结构 
const int N = 105,M = 1005;
int w[N],v[N];
int n,m;
int mx;
void dfs(int step ,int sum ,int W) {
	if(step > n) { //到终点要做的事情 
		mx = max(mx,sum);
		return ; 
	}
	if(W+w[step]<=m) dfs(step+1,sum+v[step],W+w[step]); //选 
	dfs(step+1,sum,W); //不选 
}
int f[N][M]; // f[i][j]  = > f[step][W] 
int main(){
	cin>>n>>m;
	for(int i=1;i<=n;i++) cin>>w[i]>>v[i];
	//dfs(1,0,0);
	//cout<<mx<<endl; 
	for(int i=1;i<=n;i++){
		for(int j=0;j<=m;j++){
			f[i][j] = f[i-1][j];//不选
			if(j>=w[i])  f[i][j] = max(f[i-1][j],f[i-1][j-w[i]] + v[i]);
		}
	}
	for(int i=1;i<=n;i++){
		for(int j=0;j<=m;j++)
			cout<<fixed<<setw(3)<<f[i][j]<<" ";
			cout<<endl;
	} 
	cout<<f[n][m];
			
	return 0;
}

