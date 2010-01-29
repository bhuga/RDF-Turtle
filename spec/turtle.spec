require File.join(File.dirname(__FILE__), 'spec_helper')

bad_test_files = File.join File.dirname(__FILE__), "tests", "bad", "bad*.ttl"
bad_tests = Dir.glob(bad_test_files).sort

good_test_files = File.join File.dirname(__FILE__), "tests", "good", "test*[0-9].ttl"
good_tests_list = Dir.glob(good_test_files.sort)
good_tests = {}
good_tests_list.each do |test_file|
  good_tests[test_file] = test_file.sub(/\.ttl$/,".out")
end

describe RDF::Turtle do


  context "after load" do

    it "should be an available format" do
      RDF::Format.each.should include RDF::Turtle::Format
    end

    it "should be the format for .ttl files" do
      RDF::Format.for('sample.ttl').should == RDF::Turtle::Format
    end

    it "should be the format for :turtle" do
      RDF::Format.for(:turtle).should == RDF::Turtle::Format
    end

    it "should have RDF::Turtle::Reader as its reader" do
      RDF::Turtle::Format.reader.should == RDF::Turtle::Reader
    end

    it "should have RDF::Turtle::Writer as its writer" do
      RDF::Turtle::Format.writer.should == RDF::Turtle::Writer
    end

    it "should be an available reader" do
      RDF::Reader.each.should include RDF::Turtle::Reader
    end

    it "should be defined as the reader for .ttl files" do
      RDF::Reader.for('sample.ttl').should == RDF::Turtle::Reader
    end

    it "should be defined as the reader for :turtle files" do
      RDF::Reader.for(:turtle).should == RDF::Turtle::Reader
    end
  end

  context "when reading" do
    context "a failure case"  do
      bad_tests.each do | bad_test |
        it "should fail on #{File.basename(bad_test)}" do
          lambda {RDF::Repository.load(bad_test)}.should raise_error RDF::ReaderError
        end
      end
    end

    context "a passing case" do
      good_tests.each do |input, output|
        it "should pass for #{File.basename(input)}" do
          turtle = nil
          lambda {turtle = RDF::Repository.load(input)}.should_not raise_error
          ntriples = RDF::Repository.load(output)
          turtle.should have_the_same_triples_as ntriples
        end
      end
    end

  end

  context "when serializing" do

  end

end
