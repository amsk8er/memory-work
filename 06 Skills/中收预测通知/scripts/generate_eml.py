#!/usr/bin/env python3
"""
中收预测通知 .eml 生成脚本

Usage:
    python generate_eml.py --type city --quarter "2026年一季度" --dates "3月2日,3月6日,3月13日,3月20日,3月26日,3月30日,3月31日" --actual-dates "3月2日,3月6日" --output "中间业务收入预测通知.eml"
    python generate_eml.py --type dept --quarter "2026年一季度" --dates "3月2日,3月20日" --output "中间业务收入预测通知（专业部门）.eml"

Parameters:
    --type: "city" (市分行) or "dept" (专业部门)
    --quarter: 季度描述, e.g. "2026年一季度"
    --dates: 逗号分隔的报送日期
    --actual-dates: (city only) C列填写实际数的日期
    --output: 输出文件名
    --sign-date: 落款日期, e.g. "2026年2月28日"
"""

import argparse
import calendar
import re
from email.mime.text import MIMEText


def parse_args():
    parser = argparse.ArgumentParser(description="Generate 中收预测通知 .eml")
    parser.add_argument("--type", choices=["city", "dept"], required=True)
    parser.add_argument("--quarter", required=True, help="e.g. 2026年一季度")
    parser.add_argument("--dates", required=True, help="Comma-separated reporting dates")
    parser.add_argument("--actual-dates", default="", help="Dates using actual data for C column")
    parser.add_argument("--output", required=True)
    parser.add_argument("--sign-date", default="", help="Sign-off date")
    parser.add_argument("--year-rule", default="2025", help="分润规则年份 (dept only)")
    return parser.parse_args()


def generate_calendar_html(year, month, report_dates):
    """Generate HTML calendar table with report dates marked."""
    cal = calendar.Calendar(firstweekday=0)  # Monday first
    weeks = cal.monthdayscalendar(year, month)

    header = '''<table style="border-collapse: collapse; margin: 10px 60px; font-family: 仿宋, FangSong, serif; font-size: 12pt; text-align: center;">
<tr style="background-color: #335294; color: #FFFFFF; font-family: 黑体, SimHei, sans-serif;">'''

    days = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    for d in days:
        header += f'\n<th style="border: 1px solid #999; padding: 8px 20px; width: 80px;">{d}</th>'
    header += "\n</tr>"

    rows = ""
    last_day = max(d for week in weeks for d in week if d > 0)

    for week in weeks:
        rows += "\n<tr>"
        for i, day in enumerate(week):
            if day == 0:
                rows += '\n<td style="border: 1px solid #999; padding: 8px;"></td>'
            elif day in report_dates:
                if day == last_day:
                    # Last day special: red background
                    rows += f'\n<td style="border: 1px solid #999; padding: 8px; background-color: #FFD7D7;"><b>{day} ✅</b><br><br><span style="font-size: 9pt; color: #CC0000;">18时加报</span></td>'
                else:
                    rows += f'\n<td style="border: 1px solid #999; padding: 8px; background-color: #FFF3CD;"><b>{day} ✅</b></td>'
            elif i >= 5:
                # Weekend
                rows += f'\n<td style="border: 1px solid #999; padding: 8px; color: #999;">{day}</td>'
            else:
                rows += f'\n<td style="border: 1px solid #999; padding: 8px;">{day}</td>'
        rows += "\n</tr>"

    return header + rows + "\n</table>"


def extract_day_numbers(dates_str):
    """Extract day numbers from date strings like '3月2日,3月6日'."""
    return [int(re.search(r'(\d+)日', d).group(1)) for d in dates_str.split(",") if re.search(r'(\d+)日', d)]


def generate_city_html(quarter, dates_str, actual_dates_str, sign_date, calendar_html):
    """Generate city branch notice HTML body."""
    return f'''<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"></head>
<body style="margin: 40px 60px; color: #000000;">

<p style="text-align: center; font-family: 宋体, SimSun, serif; font-size: 20pt; line-height: 1.8;">
<b>关于{quarter}中间业务收入预测安排的通知</b>
</p>

<p style="font-family: 仿宋, FangSong, serif; font-size: 14pt; line-height: 1.8;">各市分行：</p>

<p style="font-family: 仿宋, FangSong, serif; font-size: 14pt; line-height: 1.8; text-indent: 2em;">
为做好{quarter.split('年')[1]}中间业务收入组织工作，根据总行及省分行工作安排，现将相关预测事项通知如下：
</p>

<p style="font-family: 黑体, SimHei, sans-serif; font-size: 14pt; line-height: 1.8;"><b>一、预测内容</b></p>

<p style="font-family: 仿宋, FangSong, serif; font-size: 14pt; line-height: 1.8; text-indent: 2em;">
3月末中间业务毛收入及分项，手佣支出、净收入预测。其中手佣净收入需按业务条线填报明细数据。
</p>

<p style="font-family: 仿宋, FangSong, serif; font-size: 14pt; line-height: 1.8; text-indent: 2em;">
包括：手续费及佣金支出（5310科目、522012科目），以及5310手续费支出分项。
</p>

<p style="font-family: 黑体, SimHei, sans-serif; font-size: 14pt; line-height: 1.8;"><b>二、报送方式</b></p>

<p style="font-family: 仿宋, FangSong, serif; font-size: 14pt; line-height: 1.8; text-indent: 2em;">
通过邮件报送，表样见附件。
</p>

<p style="font-family: 黑体, SimHei, sans-serif; font-size: 14pt; line-height: 1.8;"><b>三、报送时间</b></p>

<p style="font-family: 仿宋, FangSong, serif; font-size: 14pt; line-height: 1.8; text-indent: 2em;">
3月预测上报时间为<span style="font-family: 黑体, SimHei, sans-serif;"><b>{dates_str}，上午10时前报送</b></span>。
</p>

<p style="font-family: 黑体, SimHei, sans-serif; font-size: 14pt; line-height: 1.8; text-indent: 2em; color: #CC0000;">
<b>3月31日晚上18时加报一次预测，C列填写17时预查询结果。</b>
</p>

<p style="font-family: 黑体, SimHei, sans-serif; font-size: 14pt; line-height: 1.8; text-indent: 2em; margin-top: 10px;">
<b>{quarter.split('年')[0]}年3月报送日历：</b>
</p>

{calendar_html}

<p style="font-family: 仿宋, FangSong, serif; font-size: 14pt; line-height: 1.8;">
注：{actual_dates_str}，C列填写2月末实际数，D至I列反映3月当月收入分项预测。
</p>

<p style="font-family: 仿宋, FangSong, serif; font-size: 14pt; line-height: 1.8; text-indent: 4em;">
其余预测日，C列填写上日实绩，逻辑同上。
</p>

<p style="font-family: 仿宋, FangSong, serif; font-size: 14pt; line-height: 1.8; text-indent: 4em;">
3月31日晚上18时报送的预测，C列填写17时预查询结果。
</p>

<p style="font-family: 黑体, SimHei, sans-serif; font-size: 14pt; line-height: 1.8;"><b>四、注意事项</b></p>

<p style="font-family: 仿宋, FangSong, serif; font-size: 14pt; line-height: 1.8; text-indent: 2em;">
①预测口径包含预计各类分润、考核还原收入（含工银理财考核还原数），信用卡总行分润不再单独报送。
</p>

<p style="font-family: 仿宋, FangSong, serif; font-size: 14pt; line-height: 1.8; text-indent: 2em;">
②如预测净收入同比下降，请以文字材料反馈原因及措施。
</p>

<br>
<p style="font-family: 仿宋, FangSong, serif; font-size: 14pt; line-height: 1.8; text-align: right; margin-right: 60px;">
省分行财务会计部<br>{sign_date}
</p>

</body>
</html>'''


def generate_dept_html(quarter, dates_list, sign_date, year_rule):
    """Generate department notice HTML body."""
    dates_section = ""
    for i, d in enumerate(dates_list):
        dates_section += f'''<p style="font-family: 仿宋, FangSong, serif; font-size: 14pt; line-height: 1.8; text-indent: 2em;">
<span style="font-family: 黑体, SimHei, sans-serif;"><b>第{["一","二","三","四","五"][i]}次：{d}上午10时前；</b></span>
</p>\n'''

    return f'''<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"></head>
<body style="margin: 40px 60px; color: #000000;">

<p style="text-align: center; font-family: 宋体, SimSun, serif; font-size: 20pt; line-height: 1.8;">
<b>关于{quarter}中间业务收入预测安排的通知</b>
</p>

<p style="font-family: 仿宋, FangSong, serif; font-size: 14pt; line-height: 1.8;">各专业部门：</p>

<p style="font-family: 仿宋, FangSong, serif; font-size: 14pt; line-height: 1.8; text-indent: 2em;">
为做好{quarter.split('年')[1]}中间业务收入相关工作，根据总行通知，请对季末中收开展预测。具体事项如下：
</p>

<p style="font-family: 黑体, SimHei, sans-serif; font-size: 14pt; line-height: 1.8;"><b>一、报送内容</b></p>

<p style="font-family: 仿宋, FangSong, serif; font-size: 14pt; line-height: 1.8; text-indent: 2em;">
填报内容：报送分科目收入/支出预测、季末下划收入预测，共两张表。
</p>

<p style="font-family: 黑体, SimHei, sans-serif; font-size: 14pt; line-height: 1.8;"><b>二、报送时间</b></p>

{dates_section}

<p style="font-family: 仿宋, FangSong, serif; font-size: 14pt; line-height: 1.8; text-indent: 2em;">
请将附表反馈本邮箱。后续预测情况如有大额变动，请及时更新。
</p>

<p style="font-family: 黑体, SimHei, sans-serif; font-size: 14pt; line-height: 1.8;"><b>三、填报提示</b></p>

<p style="font-family: 仿宋, FangSong, serif; font-size: 14pt; line-height: 1.8; text-indent: 2em;">
1、科目预测包含总行下划/分润收入、省行划转金额，含工银理财模拟考核收入累计数。按照总行关于净收入的考核要求及产品口径，表内包括部分支出科目预测，主要涉及银行卡、个金、结现等部门，请合理预测填报。
</p>

<p style="font-family: 仿宋, FangSong, serif; font-size: 14pt; line-height: 1.8; text-indent: 2em;">
2、科目分工暂按{year_rule}年分润规则。
</p>

<p style="font-family: 仿宋, FangSong, serif; font-size: 14pt; line-height: 1.8; text-indent: 2em;">
3、预测同比下降较多的科目，建议在备注栏中简要说明减收因素。
</p>

<p style="font-family: 黑体, SimHei, sans-serif; font-size: 14pt; line-height: 1.8;"><b>四、预测表样</b></p>

<p style="font-family: 仿宋, FangSong, serif; font-size: 14pt; line-height: 1.8; text-indent: 2em;">
表内附同期、上月科目收入情况，以及预测累计数和当月比较，供填报参考。
</p>

<p style="font-family: 仿宋, FangSong, serif; font-size: 14pt; line-height: 1.8; text-indent: 2em;">
感谢支持！
</p>

<p style="font-family: 仿宋, FangSong, serif; font-size: 14pt; line-height: 1.8; text-indent: 2em; color: #0563C1; text-decoration: underline;">
省分行专业部门科目预测模板-{quarter}.xlsx
</p>

<br>
<p style="font-family: 仿宋, FangSong, serif; font-size: 14pt; line-height: 1.8; text-align: right; margin-right: 60px;">
财务会计部<br>{sign_date}
</p>

</body>
</html>'''


def main():
    args = parse_args()

    year = int(re.search(r'(\d{4})', args.quarter).group(1))

    if args.type == "city":
        report_days = extract_day_numbers(args.dates)
        calendar_html = generate_calendar_html(year, 3, report_days)
        html = generate_city_html(
            args.quarter,
            args.dates,
            args.actual_dates,
            args.sign_date,
            calendar_html
        )
        subject = f"关于{args.quarter}中间业务收入预测安排的通知"
        from_addr = "省分行财务会计部 <caiwu@example.com>"
    else:
        dates_list = [d.strip() for d in args.dates.split(",")]
        html = generate_dept_html(args.quarter, dates_list, args.sign_date, args.year_rule)
        subject = f"关于{args.quarter}中间业务收入预测安排的通知"
        from_addr = "财务会计部 <caiwu@example.com>"

    msg = MIMEText(html, 'html', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = 'recipients@example.com'  # Placeholder - load from contacts
    msg['Cc'] = '"陈良元" <陈良元.江苏分行财务会计部@工商银行.icbc>, "徐捷" <徐捷.江苏分行财务会计部@工商银行.icbc>'

    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(msg.as_string())

    print(f"✅ Generated: {args.output}")


if __name__ == "__main__":
    main()
