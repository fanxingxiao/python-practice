编写伪代码并没有所谓“正确的方式”

	Initialize - 表示设置初始值

	Prompt - 表示提示用户输入

	Display - 表示输出

例:

	小费计算程序：
	
	输入：账单金额、小费比例

	处理：计算小费

	输出：小费、总金额


	测试驱动开发（TDD）：

		为每个程序设计至少4个测试计划。

	编写伪代码：

	TipCalculator.py

	Initialize bill_amount to 0

	Initialize tip_rate to 0

	Initialize tip to 0

	Initialize total to 0

	Prompt for bill_amount with "What is the bill amount?"
	
	Prompt for tip_rate with "What is the tip rate?"

	convert bill_amount type to a number

	conver tip_rate type to a number

	tip = bill_amount * (tip_rate / 100)
	
	round tip up to nearest cent

	total = bill_amount + tip
	
	Display "Tip：$", tip
	
	Display "Total：$", total 
		
	

	
	
	