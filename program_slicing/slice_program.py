from program_slicing.graph.pdg import ProgramDependenceGraph
from program_slicing.graph.parse import Lang
from program_slicing.graph.manager import ProgramGraphsManager
from program_slicing.graph.point import Point
from program_slicing.decomposition.program_slice import ProgramSlice

source_code = """
// This is a mutant program.
// Author : ysma

public class Triangle
{

    private static final int INVALID = 4;

    private static final int SCALENE = 1;

    private static final int ISOSCELES = 2;

    private static final int EQUILATERAL = 3;

    public static  int classify( int a, int b, int c )
    {
        int trian;
        if (a <= 0 || b <= 0 || c <= 0) {
            return INVALID;
        }
        trian = 0;
        if (a == b) {
            trian = trian + 1;
        }
        if (a == c) {
            trian = trian + 2;
        }
        if (b == c) {
            trian = trian + 3;
        }
        if (trian == 0) {
            if (a + b < c || a + c < b || b + c < a) {
                return INVALID;
            } else {
                return SCALENE;
            }
        }
        if (trian > 3) {
            return EQUILATERAL;
        }
        if (trian == 1 && a + b > c) {
            return ISOSCELES;
        } else {
            if (trian == 2 && a + c > b) {
                return ISOSCELES;
            } else {
                if (trian == 3 && b + c > a) {
                    return ISOSCELES;
                }
            }
        }
        return INVALID;
    }

}
"""


def get_statement_at_line(manager, line_number):
    """Retrieve the first statement at the specified line number."""
    statements = manager.get_statements_in_range(
        Point(line_number, 0), Point(line_number + 1, 0)
    )
    return statements  # Return the first statement found or None


# Example usage
manager = ProgramGraphsManager.from_source_code(source_code, Lang.JAVA)
statements_raw = get_statement_at_line(manager, 23)
statements = manager.get_affecting_statements_full(statements_raw)
print(statements)
program_slice = ProgramSlice(source_code.splitlines(), manager)
slice = program_slice.from_statements(statements)
print(slice)
