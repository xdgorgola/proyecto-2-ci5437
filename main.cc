// Game of Othello -- Example of main
// Universidad Simon Bolivar, 2012.
// Author: Blai Bonet
// Last Revision: 1/11/16
// Modified by: 

#include <iostream>
#include <limits>
#include "othello_cut.h" // won't work correctly until .h is fixed!
#include "utils.h"

#include <unordered_map>

using namespace std;

enum Condition {GEQ, GR};

unsigned expanded = 0;
unsigned generated = 0;
int tt_threshold = 32; // threshold to save entries in TT

// Transposition table (it is not necessary to implement TT)
struct stored_info_t {
    int value_;
    int type_;
    enum { EXACT, LOWER, UPPER };
    stored_info_t(int value = -100, int type = LOWER) : value_(value), type_(type) { }
};

struct hash_function_t {
    size_t operator()(const state_t &state) const {
        return state.hash();
    }
};

class hash_table_t : public unordered_map<state_t, stored_info_t, hash_function_t> {
};

hash_table_t TTable[2];

//int maxmin(state_t state, int depth, bool use_tt);
//int minmax(state_t state, int depth, bool use_tt = false);
//int maxmin(state_t state, int depth, bool use_tt = false);
int negamax(state_t state, int depth, int color, bool use_tt = false)
{
    std::cout << "Turno: " << color << std::endl;
    std::cout << "Profundidad " << depth << std::endl;
    std::cout << state << std::endl;
    if (depth == 0 || state.terminal()){
      state.print(cout);
      return color * state.value();
    } 
    int score = std::numeric_limits<int>::min();
    std::vector<state_t> moves = state.get_valid_moves(color);
    while (!moves.empty())
    {
        state_t c = moves.back(); moves.pop_back();
        std::cout << "Vamos a hijo con " << (depth - 1) << std::endl;
        score = max(score, -negamax(c, depth - 1, -color));
    }

    return score;
}


int negamax(state_t state, int depth, int alpha, int beta, int color, bool use_tt = false)
{
    std::cout << state << std::endl;
    if (depth == 0 || state.terminal()) return color * state.value();
    int score = std::numeric_limits<int>::min();
    std::vector<state_t> moves = state.get_valid_moves(color);
    while(!moves.empty())
    {
        state_t c = moves.back(); moves.pop_back();
        int val = negamax(c, depth - 1, -beta, -alpha, -color);
        score = max(score, val);
        alpha = max(alpha, val);
        if (alpha >= beta) break;
    }

    return score;
}


bool TEST(state_t state, int depth, int color, int score, Condition cond) 
{
    if (depth == 0 || state.terminal()) 
        return state.value() > score;

    bool isMax = color == 1; // Ver si es 1 o -1
    std::vector<state_t> moves = state.get_valid_moves(color);
    for (auto c: moves)
    {
        if (isMax && TEST(c, depth - 1, -color, score, Condition::GR))
            return true;
        
        if (!isMax && !TEST(c, depth - 1, -color, score, Condition::GR))
            return false;

        break;  // simulando el if first.
    }

    return !isMax;
}


int scout(state_t state, int depth, int color, bool use_tt = false)
{
    if (depth == 0 || state.terminal()){
      return state.value();
    }
        

    int score = 0;
    bool isMax = color == 1; // Ver si es 1 o -1
    bool first = true;
    std::vector<state_t> moves = state.get_valid_moves(color);
    for(auto c: moves)
    {
        if (first)
        {
            first = false;
            score = scout(c, depth -1, -color);
            continue;
        }

        if (isMax && TEST(c, depth, -color, score, Condition::GR))
            score = scout(c, depth - 1, -color);
        
        if (!isMax && !TEST(c, depth, -color, score, Condition::GEQ))
            score = scout(c, depth - 1, -color);
    }
    return score;
}


int negascout(state_t state, int depth, int alpha, int beta, int color, bool use_tt = false)
{
    if (depth == 0 || state.terminal()) return color * state.value();

    int score = 0;
    bool first = true;
    std::vector<state_t> moves = state.get_valid_moves(color);
    for(auto c: moves)
    {
        if (first)
        {
            first = false;
            score = -negascout(c, depth -1, -beta, -alpha, -color);
        }
        else
        {
            score = -negascout(c, depth - 1, -alpha - 1, -alpha, -color);
            if (alpha < score && score < beta)
                score = -negascout(c, depth - 1, -beta, -score, -color);
        }
        alpha = max(alpha, score);
        if (alpha >= beta) break;;
    }
    return alpha;
}



void prueba1(){
  state_t state;
  // &
  int black_moves [] = 
    {  4, 5, 6, 7, 8, 9 
    , 10,11,      14,15
    , 16,17,18,19,20,21
    , 22,23,24,25,26,27
    , 28,29,30,31,32,33,34,35
    };
  
  // O
  int white_moves [] = 
    {0,1,3, 10,15,17,18,19,25};
  /*

  Checks if it makes a good decision at depth 1:
  Right choice: take the right one
  +------+
  |&&&&&&|
  |O&..&O|
  |&OOO&&|
  |&&&O&&|
  |&&&&&&|
  |&&&&&&|
  +------+

  Right choice:
  +------+
  |&&&&&&|
  |OOOOOO|
  |&O&&&&|
  |&&&&&&|
  |&&&&&&|
  |&&&&&&|
  +------+

  Left choice:
  +------+
  |&&&&&&|
  |OOOOOO|
  |&&&O&&|
  |&&&O&&|
  |&&&&&&|
  |&&&&&&|
  +------+
  */
  bool black = 2 % 2 == 0; // black moves first!
  bool white = 2 % 2 != 0; // black moves first!
  for (int i=0; i < 30; i++){
    state.set_color(black, black_moves[i]);
  }

  for (int i=0; i < 6; i++){
    state.set_color(white, white_moves[i]);
  }
  
  cout << state << endl;

  cout << negamax(state,5,black) << endl;
  cout << scout(state,5,black) << endl;
  cout << negascout(state, 5, -200, 200, black);
}


void prueba2(){

  /*
  Checks if it makes a good decision at depth 2
  +------+
  |&&&O&.|
  |O&..O&|
  |&&OO&&|
  |&O&O&&|
  |&O&&&&|
  |&&&.&&|
  +------+

  Possible optimal?
  +------+
  |&&&O&&|
  |OOOO&&|
  |&&&&&&|
  |&O&O&&|
  |&O&O&&|
  |&&&O&&|
  +------+
  */
  state_t state;
  // &
  int black_moves [] = 
    {  4, 5, 6, 8, 11, 15
    , 16,17, 18,19,20,21
    , 22,23,24,25,26,27
    , 28,29,30,31,32,34,35
    };
  
  // O
  int white_moves [] = 
    {7,10,14,0,1,3,21,25};

  

  bool black = 2 % 2 == 0; // black moves first!
  bool white = 2 % 2 != 0; // black moves first!
  for (int i=0; i < 25; i++){
    state.set_color(black, black_moves[i]);
  }

  for (int i=0; i < 8; i++){
    state.set_color(white, white_moves[i]);
  }
  
  cout << state << endl;
  cout << negamax(state,5,black) << endl;
  cout << scout(state,5,black) << endl;
  cout << negascout(state, 5, -200, 200, black);
}

int main(int argc, const char **argv) {
    state_t pv[128];
    int npv = 0;
    for( int i = 0; PV[i] != -1; ++i ) ++npv;

    int algorithm = 0;
    if( argc > 1 ) algorithm = atoi(argv[1]);
    bool use_tt = argc > 2;

    // Extract principal variation of the game
    state_t state;
    cout << "Extracting principal variation (PV) with " << npv << " plays ... " << flush;
    for( int i = 0; PV[i] != -1; ++i ) {
        bool player = i % 2 == 0; // black moves first!
        int pos = PV[i];
        pv[npv - i] = state;
        state = state.move(player, pos);
    }
    pv[0] = state;
    cout << "done!" << endl;

#if 1
    prueba2();

    // print principal variation
    /* for( int i = 0; i <= npv; ++i ){
      cout << pv[npv - i] << endl;
      pv[npv - i].print_bits(cout);
      cout << endl;
    } */

    return 0;
        
#endif

    // Print name of algorithm
    cout << "Algorithm: ";
    if( algorithm == 1 )
        cout << "Negamax (minmax version)";
    else if( algorithm == 2 )
        cout << "Negamax (alpha-beta version)";
    else if( algorithm == 3 )
        cout << "Scout";
    else if( algorithm == 4 )
        cout << "Negascout";
    cout << (use_tt ? " w/ transposition table" : "") << endl;

    // Run algorithm along PV (bacwards)
    cout << "Moving along PV:" << endl;
    for( int i = 0; i <= npv; ++i ) {
        //cout << pv[i];
        int value = 0;
        TTable[0].clear();
        TTable[1].clear();
        float start_time = Utils::read_time_in_seconds();
        expanded = 0;
        generated = 0;
        int color = i % 2 == 1 ? 1 : -1;

        try {
            if( algorithm == 1 ) {
                value = negamax(pv[i], 4, color, use_tt);
            } else if( algorithm == 2 ) {
                value = negamax(pv[i], 4, -200, 200, color, use_tt);
            } else if( algorithm == 3 ) {
                value = scout(pv[i], 4, color, use_tt);
            } else if( algorithm == 4 ) {
                value = negascout(pv[i], 4, -200, 200, color, use_tt);
            }
        } catch( const bad_alloc &e ) {
            cout << "size TT[0]: size=" << TTable[0].size() << ", #buckets=" << TTable[0].bucket_count() << endl;
            cout << "size TT[1]: size=" << TTable[1].size() << ", #buckets=" << TTable[1].bucket_count() << endl;
            use_tt = false;
        }

        float elapsed_time = Utils::read_time_in_seconds() - start_time;

        cout << npv + 1 - i << ". " << (color == 1 ? "Black" : "White") << " moves: "
             << "value=" << color * value
             << ", #expanded=" << expanded
             << ", #generated=" << generated
             << ", seconds=" << elapsed_time
             << ", #generated/second=" << generated/elapsed_time
             << endl;
    }

    return 0;
}

