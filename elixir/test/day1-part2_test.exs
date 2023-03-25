defmodule Day1Part2Test do
  use ExUnit.Case

  test "solution" do
    assert Day1Part2.solve("../puzzle-input/day1-example-input.txt") == 45_000
    assert Day1Part2.solve("../puzzle-input/day1-input.txt") == 197_400
  end
end
