defmodule Day1Test do
  use ExUnit.Case

  test "solution" do
    assert Day1.solve("../puzzle-input/day1-example-input.txt") == 24_000
    assert Day1.solve("../puzzle-input/day1-input.txt") == 69_206
  end
end
