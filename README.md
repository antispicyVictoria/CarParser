# This is a simple car parser

## PLAN:

1.  Go to the root page: https://car.autohome.com.cn/pic/series-s32040/3170.html#pvareaid=3454494
2.  Get all the links to the cars from "2018 款" section. (how do we get all those links???)
3.  For each car link we do this:

    3.1. Open the car link.

    3.2. Select all the elements by this selector: "div.column.contentright.fn-visible > div:nth-child(7) > div > div > div.uibox-con > ul > li > a > img"

    3.3. For each of the selected element:

    3.3.1. Get the link to the image from attribute "src".

    3.3.2. Save the image from the link from previous step.
