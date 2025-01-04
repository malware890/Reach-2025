#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include "cpu_bound.h"


// System of Equations       Basic Tests: ___       Intermediate Tests: ___       Simulation: ___
class Term {
    public:
    char l;
    double coef;
public:
    Term(char l, double coef) : l(l), coef(coef) {};
    Term(char l) : l(l) {};
    Term() = default;
};

static std::vector<Term> parse(std::string eq) {
    std::vector<Term> terms;
    std::vector<int> spaces;
    for (int i = 0; i < eq.length(); i++) {
        if (eq[i] == ' ')
            spaces.push_back(i);
    }

    int i = 0;
    terms.push_back(Term((char) eq[spaces[0] - 1], (int) std::stol(eq.substr(0, spaces[0] - 1))));
    for (i = 1; i < spaces.size() - 1; i++) {
        
    }
    terms.push_back(Term((char) eq[eq.length() - 1], (int) std::stol(eq.substr(spaces[i] + 1, eq.length() - spaces[i] - 2))));

    return terms;
}

int main() {
    auto s = parse("25x + 2 = 81y");
    for (auto i : s)
        std::cout << i.coef << i.l << std::endl;
}

template <typename... Args>
static void solve_sys_impl(Args... args) {

}

void solve_sys() {
    solve_sys_impl();
}

// solve_sys(2, "25x + 2 = 2y", "9 - 7y = 18x + 2y")
