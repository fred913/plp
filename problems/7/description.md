# Python程序基本结构 - If Else?
课本说得好，“无论内容怎样复杂、功能如何强大的程序，都由基本结构组合而成。这些基本结构称为‘程序的控制结构’。Python程序的基本结构只有三种，即顺序结构、分支结构和循环结构。”
`if else`结构是Python基本结构中的“循环结构”。

## 分支 
`if else`的一般格式如下：  
<pre id="description-code-editor" style="height: 70px;">
if &lt;variable&gt;:
    &lt;statements&gt;  # 如果variable为真（非0，比如-1、0等）
else:
    &lt;statements&gt;  # 如果variable为假</pre>
<script>
window.dce1 = ace.edit("description-code-editor", {
    mode: "ace/mode/python",
    selectionStyle: "text",
    readOnly: true,
    fontSize: "15px",
    theme: "ace/theme/chrome"
})
</script>

###### 是不是非常的简单呢？  

## 任务目标  
小明同学准备了一个数，认为这个数是奇数。请你给个程序判断这个数是奇数还是偶数？  
 - 如果是奇数，请输出1  
 - 如果是偶数，请输出0  