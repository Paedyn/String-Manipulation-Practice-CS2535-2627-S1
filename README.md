## String Manipulation Practice

Create a Python program that processes four messy strings and produces the required output. You must start with the strings exactly as provided and use string methods to clean or reorganize them; do not simply type the corrected values yourself.

This activity uses the capitalization, whitespace removal, `split()`, `replace()`, and `join()` methods from the lesson, along with converting numeric strings using `int()` or `float()`.

### String 1 — Clean a Name

Starting string:

```python
name = "   aLeX mOrGaN   "
```

Requirements:
- Remove the extra whitespace from the beginning and end.
- Correct the capitalization so each part of the name begins with a capital letter.
- Print the finished name.

Expected output:

```text
Alex Morgan
```

### String 2 — Clean a Status Message

Starting string:

```python
status = "WARNING::ENGINE_OVERHEAT::SECTOR_7"
```

Requirements:
- Convert all letters to lowercase.
- Replace each `::` with ` | `.
- Replace each `_` with a space.
- Print the finished status message.

Expected output:

```text
warning | engine overheat | sector 7
```

### String 3 — Organize Module Names

Starting string:

```python
modules = "navigation|life_support|cargo_bay|engine_control"
```

Requirements:
- Separate the string wherever `|` appears.
- Replace the underscores in each module name with spaces.
- Format each module name using title capitalization.
- Join the module names back into one string separated by `, `.
- Print the finished string.

Expected output:

```text
Navigation, Life Support, Cargo Bay, Engine Control
```

### String 4 — Process Sensor Readings

Starting string:

```python
readings = "  18,27,35,20  "
```

Requirements:
- Remove the unnecessary whitespace.
- Separate the four values.
- Convert each value from a string into an integer.
- Calculate the total of all four readings.
- Calculate the average of the four readings.
- Print the total and average.

Expected output:

```text
Total: 100
Average: 25.0
```

---

## String Cleanup Challenge — 20 Marks

| Assessment Item                  | Criteria                                                                                                                                          |                                                                                                    Marks |
|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------:|
| ☐ String 1 — Name Cleanup       | Removes the extra whitespace, corrects the capitalization, and produces `Alex Morgan`.                                                            |                                                                                                        3 |
| ☐ String 2 — Status Message     | Converts the text to lowercase, replaces `::` with `\|`, replaces underscores with spaces, and produces the required formatted message. | 4 |
| ☐ String 3 — Module Names       | Splits the original string at `\|`, cleans each module name, applies title capitalization, and joins the values back together using `, `. | 5 |
| ☐ String 4 — Sensor Readings    | Cleans and splits the string, converts all four values to numbers, correctly calculates the total, and correctly calculates the average.          |                                                                                                        6 |
| ☐ Appropriate String Processing | Uses string methods and numeric casting to transform the provided starting strings rather than manually replacing them with the expected answers. |                                                                                                        2 |
|                                  | **Total**                                                                                                                                         |                                                                                                   **20** |

